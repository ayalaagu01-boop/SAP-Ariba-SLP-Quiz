import streamlit as st
import random
import json
import os
from datetime import datetime

# =========================================================================
# 1. ESTRUCTURA DE DATOS: Lista Completa de Preguntas (Quiz Questions) - CORREGIDA
# =========================================================================

quiz_questions = [
    {
        "question": "Your customer needs to collect detailed information from suppliers to determine if they are qualified to provide products or services in a specific category. Which SAP Ariba Supplier Management solution do you suggest?",
        "correct_answer": "SAP Ariba Supplier Lifecycle and Performance",
        "false_1": "SAP Ariba Sourcing",
        "false_2": "SAP Ariba Contracts Management",
        "false_3": "SAP Ariba Spend Analysis"
    },
    {
        "question": "What are the benefits of using SAP Ariba Supplier Risk?",
        "correct_answer": "Providing risk alerts; Mitigating supplier risks",
        "false_1": "Automating invoice processing; Managing purchase orders",
        "false_2": "Executing sourcing events; Calculating savings",
        "false_3": "Managing supplier contracts; Tracking compliance documents"
    },
    {
        "question": "Scenario: A procurement manager needs to evaluate and improve the performance of suppliers. What features in SAP Ariba Supplier Performance Management projects should be utilized?",
        "correct_answer": "Scorecards; Performance metrics; Supplier surveys",
        "false_1": "Risk control assessments; Inherent risk screening",
        "false_2": "Contract workspaces; Savings tracking",
        "false_3": "Mass registration invitations; Supplier ID management"
    },
    {
        "question": "Your customer wants to collect bank account details from their suppliers. Which type of document would you recommend?",
        "correct_answer": "External questionnaire",
        "false_1": "Internal questionnaire",
        "false_2": "Supplier request form",
        "false_3": "Engagement risk assessment"
    },
    {
        "question": "Which tasks are involved in managing supplier risk in SAP Ariba?",
        "correct_answer": "Conducting risk assessments; Developing risk mitigation plans",
        "false_1": "Approving supplier invoices; Managing supplier payments",
        "false_2": "Creating sourcing events; Awarding business",
        "false_3": "Generating spend reports; Classifying spend categories"
    },
    {
        "question": "Which elements can be included in a supplier performance survey in SAP Ariba Supplier Performance Management?",
        "correct_answer": "Feedback questions; Performance metrics",
        "false_1": "Contract terms and conditions; Bank account details",
        "false_2": "Supplier ID creation tasks; ERP integration logs",
        "false_3": "Approval workflow steps; User provisioning data"
    },
    {
        "question": "Which component is used to administer risk assessments in SAP Ariba Supplier Risk?",
        "correct_answer": "Risk management dashboard",
        "false_1": "Supplier 360 profile",
        "false_2": "Contract workspace",
        "false_3": "Sourcing Project Template"
    },
    {
        "question": "You need to use the SM Administration area to configure integration between SAP Ariba Supplier Lifecycle and Performance and an external system. Which system group do you require?",
        "correct_answer": "SM ERP Admin",
        "false_1": "SM Process Analyst",
        "false_2": "SM Integration User",
        "false_3": "Supplier Qualification Manager"
    },
    {
        "question": "Your customer wants to automatically assign approvers to supplier requests based on the supplier’s region. Which option do you recommend according to SAP Ariba’s best practice?",
        "correct_answer": "Upload a user matrix file in the SM Administration area.",
        "false_1": "Configure a simple approval rule for each region manually.",
        "false_2": "Use a custom field in the ERP system for routing.",
        "false_3": "Assign the default 'Supplier Request Approver' group to all users."
    },
    {
        "question": "Which component allows you to manage supplier contacts in SAP Ariba Supplier Lifecycle Management?",
        "correct_answer": "Contact management",
        "false_1": "Supplier Organization Profile",
        "false_2": "Supplier Risk Dashboard",
        "false_3": "Project Team Tab"
    },
    {
        "question": "When using the template upgrade feature for Supplier Management projects, which conditions must be met?",
        "correct_answer": "The supplier organization is active; None of the project’s tasks have started or all of the project’s tasks have completed.",
        "false_1": "The project is in 'Draft' status; The supplier has an active contract.",
        "false_2": "The template is a Supplier Registration template only; The supplier is Qualified.",
        "false_3": "The project must be less than 90 days old; The supplier must be on Ariba Network."
    },
    {
        "question": "Which project types in the SAP Ariba Supplier Management Portfolio use matrix-based assignments?",
        "correct_answer": "Engagement Risk projects; Supplier qualification projects",
        "false_1": "Supplier Registration projects; Contract workspaces",
        "false_2": "Supplier Request projects; Supplier Performance projects",
        "false_3": "Sourcing events; Supplier Audits"
    },
    {
        "question": "Which supplier management project type allows for multiple templates?",
        "correct_answer": "SM modular questionnaire",
        "false_1": "Supplier Registration",
        "false_2": "Supplier Performance Management",
        "false_3": "Supplier Request"
    },
    {
        "question": "On which elements of the engagement is the Residual Risk field in the engagement summary based?",
        "correct_answer": "Issues created during the engagement request process",
        "false_1": "The supplier's inherent risk score",
        "false_2": "The total contract value for the engagement",
        "false_3": "The number of users assigned to the project"
    },
    {
        "question": "Which types of optional third-party content are supported in SAP Ariba Risk?",
        "correct_answer": "Adverse media; Compliance; Financial; Environmental and social",
        "false_1": "Weather forecasts; Commodity market prices",
        "false_2": "Supplier HR data; Internal audit reports",
        "false_3": "Customer feedback scores; Product design blueprints"
    },
    {
        "question": "Your customer wants to restrict the visibility of supplier bank account and routing numbers to its accounts payable department. Which option do you recommend?",
        "correct_answer": "Use the Sensitive Data Mask Pattern field.",
        "false_1": "Apply a simple visibility condition based on the user's group.",
        "false_2": "Create a separate, internal-only questionnaire for bank details.",
        "false_3": "Store the data outside of Ariba and reference it in the profile."
    },
    {
        "question": "Scenario: A company wants to proactively manage supplier risks. What steps should be taken in SAP Ariba Supplier Risk Management?",
        "correct_answer": "Monitor risk dashboards; Conduct risk assessments; Develop risk mitigation strategies",
        "false_1": "Execute sourcing events; Negotiate new contracts",
        "false_2": "Process purchase orders; Approve invoices",
        "false_3": "Create supplier registration projects; Assign qualification categories"
    },
    {
        "question": "Scorecards in SAP Ariba Supplier Performance Management offer which of the following features?",
        "correct_answer": "Combine quantitative and qualitative KPIs; Share scorecard results with suppliers on the Ariba Network; Indicate when suppliers miss a target grade.",
        "false_1": "Calculate the inherent risk score; Trigger risk controls.",
        "false_2": "Define ERP data mapping for supplier master data; Manage user provisioning.",
        "false_3": "Automate purchase order creation; Track goods receipt status."
    },
    {
        "question": "A supplier submits an update to their registration questionnaire and an approver denies the update. What is the supplier’s registration status after the update is denied?",
        "correct_answer": "Registered",
        "false_1": "Denied",
        "false_2": "Draft",
        "false_3": "Pending Registration"
    },
    {
        "question": "Your customer wants users with the Supplier Request Manager group to provide contact information for new suppliers. Which option is available to these users?",
        "correct_answer": "Enter the contact details when completing the supplier request form.",
        "false_1": "They must send an internal questionnaire to the supplier for the details.",
        "false_2": "The contact details are automatically pulled from the ERP system.",
        "false_3": "They must be assigned the 'SM Ops Admin' group to perform this action."
    },
    {
        "question": "Which of the following are subconditions?",
        "correct_answer": "Any Are True; All Are True",
        "false_1": "At Least One Is True; Only One Is True",
        "false_2": "Must Be False; Can Be True",
        "false_3": "Is Blank; Is Not Blank"
    },
    {
        "question": "Which feature in SAP Ariba Supplier Risk Management helps monitor supplier risk levels?",
        "correct_answer": "Risk dashboards",
        "false_1": "Supplier Performance Scorecards",
        "false_2": "Contract Workspaces",
        "false_3": "Sourcing Events"
    },
    {
        "question": "Which actions can be completed in the Qualification area of the supplier 360 view?",
        "correct_answer": "View the current status of qualifications started for the supplier; Start the requalification process for disqualified and expired categories.",
        "false_1": "Modify the supplier's registration data; Approve a supplier request.",
        "false_2": "Run a sourcing event for the qualified category; Create a contract.",
        "false_3": "View the supplier's risk exposure score; Update the supplier's preferred status."
    },
    {
        "question": "Which tasks can be performed in the contact management component of SAP Ariba Supplier Lifecycle Management?",
        "correct_answer": "Adding new supplier contacts; Updating contact information",
        "false_1": "Approving supplier registration; Calculating performance metrics",
        "false_2": "Defining risk categories; Setting up risk thresholds",
        "false_3": "Assigning qualification categories; Disqualifying a supplier"
    },
    {
        "question": "You are creating a new Supplier Performance Management project template from scratch. Which elements does SAP Ariba support on the Documents tab?",
        "correct_answer": "Folder; Analytical report",
        "false_1": "Contract document; Sourcing event document",
        "false_2": "Supplier registration form; Supplier risk control definition file",
        "false_3": "ERP integration mapping file; User provisioning file"
    },
    {
        "question": "Scenario: A company wants to improve supplier performance and track it over time. Which steps should be taken in SAP Ariba Supplier Performance Management?",
        "correct_answer": "Develop supplier surveys; Create performance scorecards; Define performance metrics",
        "false_1": "Define risk exposure thresholds; Monitor adverse media alerts",
        "false_2": "Configure data mappings to the ERP; Import supplier IDs",
        "false_3": "Create a sourcing event; Negotiate contract terms"
    },
    {
        "question": "Which solution from the SAP Ariba Supplier Management Portfolio is unavailable for customers that currently subscribe to SAP Ariba Supplier Information and Performance Management?",
        "correct_answer": "SAP Ariba Network Supplier Services; SAP Ariba Supply Chain Collaboration for Buyers",
        "false_1": "SAP Ariba Supplier Lifecycle and Performance; SAP Ariba Supplier Risk",
        "false_2": "SAP Ariba Sourcing; SAP Ariba Contracts",
        "false_3": "SAP Ariba Procurement Content; SAP Ariba Buying"
    },
    {
        "question": "Which supplier data elements can be imported via SM Administration?",
        "correct_answer": "Primary supplier managers for each organization; Supplier qualification statuses; Organizations from outside of SAP Ariba",
        "false_1": "Historical transaction data; Contract compliance scores",
        "false_2": "Supplier's active contracts; Details of sourcing awards",
        "false_3": "Supplier's bank account details; Sensitive risk information"
    },
    {
        "question": "Scenario: A company wants to maintain a clean core in their ERP system to maximize business process agility. What steps should be taken?",
        "correct_answer": "Minimize system customizations; Ensure system flexibility; Reduce adaptation efforts",
        "false_1": "Maximize the use of custom code; Increase system complexity",
        "false_2": "Use a heavily modified on-premise system; Avoid cloud solutions",
        "false_3": "Delegate all process logic to Ariba; Disable all ERP system reporting"
    },
    {
        "question": "Which features are part of the Supplier Qualification process in SAP Ariba Supplier Lifecycle Management?",
        "correct_answer": "Supplier information collection; Risk assessment",
        "false_1": "Invoice approval workflow; Payment processing",
        "false_2": "Sourcing event creation; Bid evaluation",
        "false_3": "Contract document management; Savings tracking"
    },
    {
        "question": "What are the benefits of using conditions in SAP Ariba templates?",
        "correct_answer": "To control the visibility of documents, folders, and tasks; To control the visibility of project groups on the Team tab",
        "false_1": "To automatically calculate performance scores; To define the supplier's risk exposure level",
        "false_2": "To set recurring schedules for phases; To map data fields to the ERP system",
        "false_3": "To define the approval flow for simple rules; To track changes to supplier records"
    },
    # ------------------ PREGUNTA CORREGIDA AQUÍ ------------------
    {
        "question": "Which component is crucial for tracking supplier performance in SAP Ariba Supplier Performance Management projects?",
        "correct_answer": "Performance scorecards",
        "false_1": "Supplier Registration Questionnaires",
        "false_2": "Risk Control Definitions File",
        "false_3": "User Matrix File" 
    },
    # ------------------ FIN PREGUNTA CORREGIDA ------------------
    {
        "question": "Your customer wants to measure how well their direct materials suppliers comply with their contract terms. They want to report on each supplier’s overall compliance score, plus specific measurements, such as on time delivery and defective parts per million. How do you suggest the customer structure their scorecard?",
        "correct_answer": "Create a report including each measure and map the KPIs to the report.",
        "false_1": "Create a separate performance survey for each measure (on time delivery, defective parts).",
        "false_2": "Use a single qualitative KPI for the overall compliance score.",
        "false_3": "Map all contract terms directly to the inherent risk screening questionnaire."
    },
    {
        "question": "What is the purpose of managing user groups in SAP Ariba Supplier Lifecycle Management?",
        "correct_answer": "To assign roles and permissions to users",
        "false_1": "To define commodity hierarchies for qualification",
        "false_2": "To control the data synchronization with the ERP system",
        "false_3": "To track supplier performance scores over time"
    },
    {
        "question": "Where should you modify an existing KPI hierarchy according to SAP Ariba’s best practices?",
        "correct_answer": "In a project-level master scorecard; In the sourcing library",
        "false_1": "Directly in the supplier’s active performance project.",
        "false_2": "Through a configuration file in the SM Administration area.",
        "false_3": "In the ERP system master data tables."
    },
    {
        "question": "What tasks can be performed during the administration of SAP Ariba Supplier Lifecycle Management?",
        "correct_answer": "Importing supplier records; Setting up supplier IDs",
        "false_1": "Approving supplier invoices; Managing payment runs",
        "false_2": "Creating new sourcing projects; Publishing RFPs",
        "false_3": "Configuring risk categories; Setting risk thresholds"
    },
    {
        "question": "Your customer is loading a large group of legacy suppliers as part of their implementation. They want to use the mass registration invitations option but have concerns with sending all of the invitations at once. Which option do you recommend?",
        "correct_answer": "Import all legacy suppliers, then upload waves to send the invitations to multiple subsets of the suppliers.",
        "false_1": "Send all invitations at once and instruct the suppliers to ignore them if they are not ready.",
        "false_2": "Use the manual single-supplier invitation process for all legacy suppliers.",
        "false_3": "The mass invitation feature does not support subsets, so all must be sent at once."
    },
    {
        "question": "The business details questionnaire requires questions of types Commodity, Region, and Department. Which functionalities are dependent upon these questions?",
        "correct_answer": "Triggering the appearance of content in the inherent risk screening questionnaire; Controlling members of project groups on the Team tab when using buyer category assignments.",
        "false_1": "Defining the supplier's payment terms; Specifying the contract's governing law.",
        "false_2": "Setting the supplier's initial registration status; Approving the supplier request.",
        "false_3": "Calculating the supplier's overall performance score; Tracking the supplier's spend."
    },
    {
        "question": "Which content type within a survey provides the most granular scores when mapped to a KPI?",
        "correct_answer": "Question",
        "false_1": "Section",
        "false_2": "Folder",
        "false_3": "Document"
    },
    {
        "question": "Your customer is using SAP Ariba Supplier Lifecycle and Performance, and wants suppliers to accept a code of conduct each year outside of the registration process. Which option do you recommend?",
        "correct_answer": "Modular questionnaire",
        "false_1": "Internal questionnaire",
        "false_2": "Supplier Performance survey",
        "false_3": "Contract amendment project"
    },
    {
        "question": "What features can be utilized in SAP Ariba Supplier Performance Management projects to evaluate suppliers?",
        "correct_answer": "Scorecards; Supplier surveys",
        "false_1": "Risk control assessments; Risk exposure reports",
        "false_2": "Sourcing events; Bid comparisons",
        "false_3": "Contract negotiation documents; Payment schedules"
    },
    {
        "question": "What is the purpose of importing supplier records in SAP Ariba Supplier Lifecycle Management?",
        "correct_answer": "To onboard and manage supplier data",
        "false_1": "To execute payment runs to the suppliers",
        "false_2": "To calculate the total spend with the supplier",
        "false_3": "To create new sourcing projects for the supplier"
    },
    {
        "question": "What is the main purpose of workspace templates in SAP Ariba Supplier Performance Management?",
        "correct_answer": "To standardize and streamline project creation",
        "false_1": "To manage supplier contact information and updates",
        "false_2": "To define the data mapping for ERP integration",
        "false_3": "To calculate the supplier's inherent risk score"
    },
    {
        "question": "Which component in SAP Ariba Supplier Lifecycle Management helps categorize suppliers based on their qualification status?",
        "correct_answer": "Supplier qualification categories",
        "false_1": "Risk assessment module",
        "false_2": "Supplier Request form",
        "false_3": "Supplier Registration questionnaire"
    },
    {
        "question": "Which of the following is a characteristic of a simple workflow in a control-based engagement risk assessment project?",
        "correct_answer": "All assessments are sent to recipients at the same time.",
        "false_1": "The assessments are sent sequentially based on the approver group.",
        "false_2": "Only one assessment can be active at any given time.",
        "false_3": "The workflow must be manually triggered for each recipient."
    },
    {
        "question": "Which feature can you use to ensure a process flow is followed in the correct order?",
        "correct_answer": "Phases",
        "false_1": "Tasks",
        "false_2": "Documents",
        "false_3": "Conditions"
    },
    {
        "question": "Scenario: A procurement manager wants to update contact information for several suppliers. What functionalities in SAP Ariba Supplier Lifecycle Management should be used?",
        "correct_answer": "Supplier onboarding; Contact management; Supplier contact updates",
        "false_1": "Sourcing events; Contract administration",
        "false_2": "Risk assessment module; Risk mitigation planning",
        "false_3": "Invoice processing; Payment reconciliation"
    },
    {
        "question": "What information is available when you view the alert list in SAP Ariba Supplier Risk?",
        "correct_answer": "A link to the information that triggered each alert; An indication of whether each alert is positive or negative; The incident type for each alert",
        "false_1": "The supplier's total spend amount; The date of the last contract renewal.",
        "false_2": "The name of the user who last edited the supplier profile; The date of the next performance review.",
        "false_3": "The supplier's full registration questionnaire responses; The calculated performance score."
    },
    {
        "question": "Your customer creates a new assessment, but notices that it’s not appearing in their engagement projects. What additional step should they take?",
        "correct_answer": "Update the risk control definitions file.",
        "false_1": "Set the assessment status to 'Active' in the Sourcing library.",
        "false_2": "Map the assessment to a KPI in the performance scorecard.",
        "false_3": "Assign the 'SM Process Analyst' group to the project team."
    },
    {
        "question": "Your customer wants to trigger risk controls in supplier risk engagement projects based on responses to questions from the inherent risk screening questionnaire. Which option do you recommend?",
        "correct_answer": "Map each question to a question ID.",
        "false_1": "Map the question directly to a custom field in the supplier database.",
        "false_2": "Create a simple approval rule based on the question response.",
        "false_3": "Define a visibility condition on the risk control task."
    },
    {
        "question": "You create a new Supplier Performance Management project and want to display the supplier’s name in the title of all future occurrences. Where would you go to make this change?",
        "correct_answer": "To the Supplier Performance Management project template",
        "false_1": "To the supplier's 360° profile",
        "false_2": "To the SM Administration area configuration files",
        "false_3": "In the ERP system master data"
    },
    {
        "question": "What are the benefits of using standard features in SAP Ariba Supplier Risk Management?",
        "correct_answer": "Real-time risk assessment; Risk mitigation strategies",
        "false_1": "Automated contract authoring; Spend categorization reports",
        "false_2": "Invoice reconciliation; Payment tracking",
        "false_3": "Sourcing event creation; Bid analysis"
    },
    {
        "question": "Which elements can be included in a workspace template in SAP Ariba Supplier Lifecycle Management?",
        "correct_answer": "Performance metrics; Project tasks",
        "false_1": "Supplier bank account details; Sensitive tax information",
        "false_2": "Final contract documents; Negotiation history",
        "false_3": "ERP system configuration settings; User password policies"
    },
    {
        "question": "Which feature allows users to evaluate supplier performance over time in SAP Ariba Supplier Performance Management?",
        "correct_answer": "Scorecards",
        "false_1": "Registration Questionnaires",
        "false_2": "Risk Dashboards",
        "false_3": "Contract Workspaces"
    },
    {
        "question": "The Evidence Collection and Risk Control Effectiveness Review phases do not contain any tasks in the supplier risk engagement project template. Which action initiates these phases?",
        "correct_answer": "Sending assessment questionnaires to recipients in the previous phase",
        "false_1": "The project is manually moved to the next phase by the project owner.",
        "false_2": "A final contract document is approved.",
        "false_3": "The supplier updates their registration details."
    },
    {
        "question": "Which of the following templates are available in SAP Ariba Supplier Information and Performance Management?",
        "correct_answer": "Supplier qualification; Preferred supplier management; Supplier registration",
        "false_1": "Engagement Risk assessment; Modular questionnaire",
        "false_2": "Contract Workspace (Procurement); Sourcing Request",
        "false_3": "Supplier Audit project; Supplier Development plan"
    },
    {
        "question": "On which screen are the response start and end dates configured for surveys in a Supplier Performance Management project?",
        "correct_answer": "Rules",
        "false_1": "Documents",
        "false_2": "Team",
        "false_3": "Phases"
    },
    {
        "question": "Which tasks can be managed within a Supplier Performance Management project in SAP Ariba?",
        "correct_answer": "Conducting supplier evaluations; Defining performance metrics",
        "false_1": "Managing supplier contacts; Setting up supplier IDs",
        "false_2": "Configuring risk thresholds; Monitoring risk alerts",
        "false_3": "Approving supplier requests; Sending registration invitations"
    },
    {
        "question": "Scenario: A procurement manager wants to ensure seamless integration with the company's ERP system. What activities should be prioritized in SAP Ariba Supplier Lifecycle Management?",
        "correct_answer": "Configuring data mappings; Setting up data synchronization schedules; Importing supplier records",
        "false_1": "Creating complex custom forms; Minimizing system flexibility",
        "false_2": "Creating new performance scorecards; Running supplier surveys",
        "false_3": "Monitoring adverse media; Developing risk mitigation plans"
    },
    {
        "question": "While reviewing a supplier request, an approver determines that there is not enough information to make an approval decision. Which option does the approver have to obtain this information?",
        "correct_answer": "Click the Request Additional Info button to re-engage the requester.",
        "false_1": "Deny the request immediately and ask the requester to start over.",
        "false_2": "Manually edit the supplier request form to add the missing data.",
        "false_3": "Send an internal performance survey to the supplier."
    },
    {
        "question": "Your customer has configured pre-grading in their survey. After receiving responses from internal participants, the supplier’s score for Innovation/Technology is below the Target Grade value. What happens next?",
        "correct_answer": "The score is highlighted to indicate that it is below the target.",
        "false_1": "The project is automatically stopped and an issue is created.",
        "false_2": "The supplier is automatically disqualified for the relevant category.",
        "false_3": "The score is automatically changed to the Target Grade value."
    },
    {
        "question": "Which feature allows users to customize workspace templates in SAP Ariba Supplier Lifecycle Management?",
        "correct_answer": "Template configuration",
        "false_1": "SM Administration User Matrix",
        "false_2": "Sourcing Library Content",
        "false_3": "Data Import Tool"
    },
    {
        "question": "Which options are available for integrating SAP Ariba Supplier Management solutions with an external system?",
        "correct_answer": "SAP Ariba SOAP web services APIs; SAP Ariba Cloud Integration Gateway; SAP Ariba Integration Toolkit",
        "false_1": "Direct SQL database connection; Custom third-party SFTP transfers",
        "false_2": "Manual data entry only; XML file uploads only",
        "false_3": "Ariba Network standard PO/Invoice integration only"
    },
    {
        "question": "Your customer wants to implement governance checks on suppliers based on their internal control policies. Which SAP Ariba solution do you recommend?",
        "correct_answer": "SAP Ariba Supplier Risk",
        "false_1": "SAP Ariba Supplier Performance Management",
        "false_2": "SAP Ariba Sourcing",
        "false_3": "SAP Ariba Contracts"
    },
    {
        "question": "Scenario: A company needs to import and manage supplier data efficiently. What steps should be taken in SAP Ariba Supplier Lifecycle Management?",
        "correct_answer": "Configure data mappings; Import supplier records; Set up supplier IDs",
        "false_1": "Run sourcing events; Negotiate new contracts; Approve invoices",
        "false_2": "Define risk categories; Monitor third-party risk alerts; Create mitigation plans",
        "false_3": "Create performance scorecards; Develop supplier surveys; Define KPIs"
    },
    {
        "question": "Which mandatory steps are needed to use buyer category assignments?",
        "correct_answer": "Upload a user matrix in SM Administration; Enable “use commodity and region assignments” in project groups.",
        "false_1": "Enable the 'Preferred Supplier Management' feature; Use only simple approval rules.",
        "false_2": "Configure a risk assessment for every category; Map the category to an ERP system field.",
        "false_3": "Use a modular questionnaire only; Disable all phases in the project template."
    },
    {
        "question": "Your customer wants suppliers to include hyphens between segments of their contact phone numbers when completing the external registration questionnaire. Which option do you recommend?",
        "correct_answer": "Use the Validation Pattern field to specify the format of the response.",
        "false_1": "Set the question type to 'Text Area' to allow any format.",
        "false_2": "Apply a visibility condition to force a specific length.",
        "false_3": "Enable the 'Search term' feature for the question."
    },
    {
        "question": "What is a key benefit of using SAP Ariba Supplier Lifecycle Management?",
        "correct_answer": "Enhanced supplier qualification processes",
        "false_1": "Automated creation of purchase orders",
        "false_2": "Real-time spend analysis reporting",
        "false_3": "Centralized contract price negotiation"
    },
    {
        "question": "Which of the following are characteristics of a periodic recurring phase in an SAP Ariba Supplier Performance Management project?",
        "correct_answer": "Periodic scorecards and surveys are created from the master documents; The title of the new phase contains the month and year of the occurrence.",
        "false_1": "The phase starts automatically when the previous phase is completed; Only qualitative KPIs can be used.",
        "false_2": "The phase requires manual creation for each new recurrence; The title is always the same as the template phase title.",
        "false_3": "Only external participants can respond to surveys in this phase; Risk controls are always triggered."
    },
    {
        "question": "Scenario: A company needs to ensure that only authorized users can access certain supplier data. What steps should be taken in SAP Ariba Supplier Lifecycle Management?",
        "correct_answer": "Define access controls; Assign roles to user groups; Create user groups",
        "false_1": "Configure risk exposure thresholds; Monitor third-party risk data",
        "false_2": "Develop new performance surveys; Create custom KPIs",
        "false_3": "Map data fields to the ERP system; Set up data synchronization schedules"
    },
    {
        "question": "Which groups should your customer consider removing from users if they want to reduce their user licenses in SAP Ariba Supplier Lifecycle and Performance?",
        "correct_answer": "Sensitive Data Access; Supplier Qualification Manager",
        "false_1": "Supplier Request Manager; SM Process Analyst",
        "false_2": "SM ERP Admin; SM Ops Admin",
        "false_3": "Report Administrator; Contact Management User"
    },
    {
        "question": "Your customer wants to include a system group or project group in the approval flow for a new supplier. Which of the following is a limitation with a simple approval rule for SAP Ariba templates?",
        "correct_answer": "The system will accept the approval from a single user within the group.",
        "false_1": "The rule can only be based on one condition at a time.",
        "false_2": "A simple approval rule cannot use system or project groups.",
        "false_3": "The approval must always go to the SM Process Analyst group."
    },
    {
        "question": "Which attributes of Importance should be considered when creating a scoring structure within a survey?",
        "correct_answer": "Acceptable values range between 0 and 10; The value defines a question’s relative importance within a section.",
        "false_1": "Acceptable values range between 1 and 100; The value defines the total weight of the survey in the scorecard.",
        "false_2": "It is a mandatory field for every question; It determines the visibility of the question.",
        "false_3": "It is used to map the question to the ERP master data; The value must be set to 1 for all questions."
    },
    {
        "question": "Scenario: A company needs to classify and manage different types of supplier risks. What steps should be taken in SAP Ariba Supplier Risk Administration?",
        "correct_answer": "Define risk categories; Set up risk thresholds; Configure risk assessments",
        "false_1": "Create performance scorecards; Define performance metrics; Develop surveys",
        "false_2": "Configure data mappings to the ERP; Import supplier IDs; Set up data synchronization",
        "false_3": "Run sourcing events; Award contracts; Track savings"
    },
    {
        "question": "You configure the supplier database field mappings and want confirmation that a field has been mapped correctly. What action would you take to validate field mapping entries?",
        "correct_answer": "Enable synching between SAP ERP and SAP Ariba.",
        "false_1": "Manually check the supplier profile in Ariba for the updated data.",
        "false_2": "Run a standard spend analysis report.",
        "false_3": "Create a new contract workspace and see if the field is present."
    },
    {
        "question": "Scenario: A company needs to evaluate supplier performance based on feedback and historical data. What steps should be taken in SAP Ariba Supplier Performance Management?",
        "correct_answer": "Define performance metrics; Develop scorecards; Create and distribute surveys",
        "false_1": "Define inherent risk; Create risk mitigation plans; Monitor adverse media",
        "false_2": "Create a new supplier request; Invite the supplier to register",
        "false_3": "Negotiate contract terms; Approve the final contract document"
    },
    {
        "question": "What tasks can be performed during the administration of SAP Ariba Supplier Risk?",
        "correct_answer": "Administering risk assessments; Configuring risk categories",
        "false_1": "Approving supplier registration updates; Managing supplier contacts",
        "false_2": "Defining KPIs for performance scorecards; Setting survey rules",
        "false_3": "Creating and publishing sourcing events; Evaluating bids"
    },
    {
        "question": "What is the primary objective of Supplier Risk Management in SAP Ariba?",
        "correct_answer": "To mitigate and manage supplier risks",
        "false_1": "To track supplier savings targets",
        "false_2": "To automate the procurement to pay process",
        "false_3": "To centralize all supplier contracts"
    },
    {
        "question": "Which action enables the evaluation of a supplier for a preferred status level?",
        "correct_answer": "A qualification for the supplier is fully approved.",
        "false_1": "The supplier's registration is approved.",
        "false_2": "The supplier has a risk score below the high threshold.",
        "false_3": "The supplier has an active contract."
    },
    {
        "question": "Which of the following actions can you perform using phases?",
        "correct_answer": "Notify users when the phase due date has passed; Set recurring schedules.",
        "false_1": "Define the approval flow for simple approval rules; Map data fields to the ERP.",
        "false_2": "Control the visibility of documents and folders; Determine the supplier's qualification status.",
        "false_3": "Create new KPIs for a scorecard; Import supplier master data."
    },
    {
        "question": "What benefits do scorecards provide in SAP Ariba Supplier Performance Management?",
        "correct_answer": "Improved supplier evaluation; Historical performance tracking",
        "false_1": "Real-time risk monitoring; Adverse media alerts",
        "false_2": "Automated purchase order creation; Inventory management",
        "false_3": "Tracking contract end dates; Managing contract amendments"
    },
    {
        "question": "Your customer's functional buyer identifies potential new suppliers for laptops. Based on SAP Ariba’s best practice, which SAP Ariba Supplier Lifecycle and Performance system group do you assign to the functional buyer?",
        "correct_answer": "Supplier Request Manager",
        "false_1": "SM ERP Admin",
        "false_2": "Supplier Qualification Manager",
        "false_3": "Sensitive Data Access"
    },
    {
        "question": "What are the benefits of maintaining a clean core in ERP systems?",
        "correct_answer": "Increased system agility; Reduced adaptation efforts",
        "false_1": "Higher cost of maintenance; Increased system customizations",
        "false_2": "Reduced need for cloud solutions; Decentralized data management",
        "3": "Slower update cycles; Decreased flexibility"
    },
    {
        "question": "What is the purpose of configuring risk categories in SAP Ariba Supplier Risk?",
        "correct_answer": "To classify and manage different types of risk",
        "false_1": "To define the supplier's performance metrics",
        "false_2": "To control user access permissions",
        "false_3": "To set up the supplier ID format"
    },
    {
        "question": "You need to invite suppliers and internal participants to the same survey but would like to restrict their views. How do you achieve this?",
        "correct_answer": "Use visibility conditions on each question",
        "false_1": "Create two separate surveys for internal and external participants.",
        "false_2": "Assign different project groups to the supplier and the internal user.",
        "false_3": "Use a simple workflow instead of an advanced workflow."
    },
    {
        "question": "Your customer needs to initiate and manage supplier registrations, qualifications, and disqualifications. Which SAP Ariba Supplier Lifecycle and Performance system groups do you assign to a category buyer?",
        "correct_answer": "Supplier Registration Manager; Supplier Qualification Manager",
        "false_1": "SM ERP Admin; Sensitive Data Access",
        "false_2": "SM Process Analyst; Report Administrator",
        "false_3": "Supplier Request Manager; SM Ops Admin"
    },
    {
        "question": "What is the primary purpose of using surveys in SAP Ariba Supplier Performance Management?",
        "correct_answer": "To collect feedback on supplier performance",
        "false_1": "To define the supplier's contract terms",
        "false_2": "To track spend against a budget",
        "false_3": "To generate purchase orders"
    },
    {
        "question": "Which of the following components can supplier risk managers modify in the risk exposure configuration interface?",
        "correct_answer": "The relative weight of each risk category; The incident types that trigger email notifications; Low, medium, and high exposure risk thresholds.",
        "false_1": "The supplier's registration status; The supplier's contact information.",
        "false_2": "The content of the performance scorecard; The supplier performance KPIs.",
        "false_3": "The data mapping to the ERP system; The user matrix file."
    },
    {
        "question": "You are creating a new Supplier Performance Management project template from scratch. Which elements does SAP Ariba support on the Documents tab?",
        "correct_answer": "Analytical report; Folder",
        "false_1": "ERP integration logs; Supplier ID management report",
        "false_2": "Contract document; Sourcing event bid sheet",
        "false_3": "Risk control definition file; User provisioning report"
    },
    {
        "question": "What benefits does the Preferred Suppliers component provide in SAP Ariba Supplier Lifecycle Management?",
        "correct_answer": "Streamlined procurement processes; Improved supplier selection",
        "false_1": "Automated invoice payments; Real-time payment tracking",
        "false_2": "Lowered supplier risk exposure; Real-time risk alerts",
        "false_3": "Centralized contract negotiation; Legal document storage"
    },
    {
        "question": "A supplier risk manager is viewing the Supplier Risk tab in SAP Ariba. Which components are available to review risk information?",
        "correct_answer": "A risk exposure report that compares the exposure scores of followed suppliers; A risk summary tile to see an overview of risk levels for followed suppliers; A supplier feed showing newly added suppliers.",
        "false_1": "The supplier's performance scorecard; The list of all past sourcing events with the supplier.",
        "false_2": "The supplier's contract terms and conditions; The payment history.",
        "false_3": "The list of all open supplier requests; The supplier's registration status history."
    },
    {
        "question": "A supplier is invited to start a qualification. Which activity does the supplier perform first before appearing in Qualified status?",
        "correct_answer": "Submit a response to the questionnaire",
        "false_1": "Sign a contract with your company.",
        "false_2": "Get a risk score below the low threshold.",
        "false_3": "Be approved in a sourcing event."
    },
    {
        "question": "A company needs to import and manage supplier data efficiently. What steps should be taken in SAP Ariba Supplier Lifecycle Management?",
        "correct_answer": "Set up supplier IDs; Import supplier records; Configure data mappings",
        "false_1": "Create performance scorecards; Define performance metrics; Develop surveys",
        "false_2": "Run sourcing events; Award contracts; Track savings",
        "false_3": "Define risk categories; Set up risk thresholds; Configure risk assessments"
    },
    {
        "question": "Which of the following actions are available from the registration area in the supplier 360° profile?",
        "correct_answer": "Invite or re-invite a new supplier to register; See the answers to the registration questionnaires; Track the progress of the registration on the status graph.",
        "false_1": "Disqualify the supplier for a category; Start a new performance review.",
        "false_2": "Update the supplier's risk exposure settings; View adverse media alerts.",
        "false_3": "Create a new contract workspace; Send a new purchase order."
    },
    {
        "question": "When configuring phases in the supplier risk engagement project template, which step is mandatory to ensure that the task workflow is triggered correctly?",
        "correct_answer": "Set the “Choose where the tasks in this phase should be applied” option to the appropriate phase name.",
        "false_1": "Map the project to an existing contract workspace.",
        "false_2": "Ensure the template is set to 'Simple Workflow'.",
        "false_3": "Disable all visibility conditions on the tasks."
    },
    {
        "question": "Which tasks can be managed within a Supplier Performance Management project in SAP Ariba?",
        "correct_answer": "Defining performance metrics; Conducting supplier evaluations",
        "false_1": "Configuring risk thresholds; Monitoring third-party risk data",
        "false_2": "Approving supplier registration requests; Managing supplier contacts",
        "false_3": "Creating purchase orders; Processing invoices"
    },
    {
        "question": "Which tasks are involved in managing a clean core in ERP systems?",
        "correct_answer": "Minimizing customizations; Ensuring system flexibility",
        "false_1": "Maximizing custom code; Increasing data redundancy",
        "false_2": "Using only on-premise solutions; Avoiding cloud integration",
        "false_3": "Implementing complex legacy interfaces; Delaying system updates"
    },
    {
        "question": "Scenario: A procurement manager wants to enhance the supplier qualification process and mitigate supplier risks. Which SAP Ariba solutions should be utilized?",
        "correct_answer": "SAP Ariba Supplier Performance Management; SAP Ariba Supplier Risk; SAP Ariba Supplier Lifecycle Management",
        "false_1": "SAP Ariba Sourcing; SAP Ariba Contracts; SAP Ariba Spend Analysis",
        "false_2": "SAP Ariba Buying; SAP Ariba Invoice Management; SAP Ariba Catalog",
        "false_3": "SAP Ariba Supply Chain Collaboration; SAP Ariba Guided Buying"
    },
    {
        "question": "Which principle is crucial for maintaining a clean core in ERP systems?",
        "correct_answer": "Minimizing system customizations",
        "false_1": "Maximizing system complexity",
        "false_2": "Using only standard SAP functionality without any cloud extension",
        "false_3": "Storing all master data only within the ERP"
    },
    {
        "question": "Which is an additional benefit of SAP Ariba Supplier Lifecycle and Performance compared to SAP Ariba Supplier Information and Performance Management?",
        "correct_answer": "Unified vendor model for suppliers",
        "false_1": "Supplier self-service portal access",
        "false_2": "Ability to use template-based projects",
        "false_3": "Integration with SAP ERP via CIG"
    },
    {
        "question": "Which product in SAP Ariba's Spend Management portfolio focuses on managing supplier risk?",
        "correct_answer": "SAP Ariba Supplier Risk",
        "false_1": "SAP Ariba Sourcing",
        "false_2": "SAP Ariba Contracts",
        "false_3": "SAP Ariba Buying"
    },
    {
        "question": "What tasks can be performed during the administration of SAP Ariba Supplier Lifecycle Management?",
        "correct_answer": "Importing supplier records; Setting up supplier IDs",
        "false_1": "Running supplier performance surveys; Creating scorecards",
        "false_2": "Creating new sourcing events; Approving bids",
        "false_3": "Monitoring third-party risk alerts; Defining risk categories"
    },
    {
        "question": "Which component is used to set up supplier IDs in SAP Ariba Supplier Lifecycle Management?",
        "correct_answer": "Supplier ID management",
        "false_1": "SM ERP Admin",
        "false_2": "Supplier Registration Questionnaire",
        "false_3": "Contact Management"
    },
    {
        "question": "Which data source is mapped to the KPI to send quantitative data scores to a scorecard?",
        "correct_answer": "Event",
        "false_1": "Survey",
        "false_2": "Questionnaire",
        "false_3": "Contract"
    },
    {
        "question": "Which type of SAP Ariba project can engagement risk projects be associated with?",
        "correct_answer": "Contract workspace (procurement)",
        "false_1": "Supplier Performance Management project",
        "false_2": "Sourcing Request project",
        "false_3": "Supplier Registration project"
    },
    {
        "question": "Your customer leaves a survey-based KPI unmapped in the Supplier Performance Management template. How will this impact their process?",
        "correct_answer": "The owner of the scorecard can enter the KPI’s value manually.",
        "false_1": "The project will fail to publish with an error.",
        "false_2": "The scorecard will automatically pull the value from the ERP system.",
        "false_3": "The supplier must provide the value during registration."
    },
    {
        "question": "Your customer wants to ask a different set of questions for supplier qualifications in North America, South America, and Europe. How do you configure these questions in your customer's Supplier Qualification Project template?",
        "correct_answer": "Create separate modular questionnaires to be sent to suppliers during the qualification process",
        "false_1": "Use visibility conditions on a single, long qualification questionnaire.",
        "false_2": "Create a separate qualification project template for each region.",
        "false_3": "Map the region field to an ERP system to trigger the correct questions."
    },
    {
        "question": "What are the benefits of using SAP Ariba Supplier Risk?",
        "correct_answer": "Mitigating supplier risks; Providing risk alerts",
        "false_1": "Automating purchase order creation; Tracking goods receipts",
        "false_2": "Centralizing contract negotiation; Tracking contract savings",
        "false_3": "Managing supplier contacts; Setting up supplier IDs"
    },
    {
        "question": "What are the benefits of using an approver lookup table in SAP Ariba templates?",
        "correct_answer": "A range of values can be used to assign approvers; The system assigns approvers based on project field values; More than one project field value can be used to add approvers.",
        "false_1": "The approval flow is always simple and linear; It overrides all visibility conditions.",
        "false_2": "It can only be used for the first step of the approval flow; It requires manual updates in the template.",
        "false_3": "It is only available in Supplier Registration projects; It cannot use system groups."
    },
    {
        "question": "You applied an update to the Team Member Rules file in a Supplier Performance Management project template and published. However, the project you created two weeks ago does NOT reflect this updated file. Why is this the case?",
        "correct_answer": "The template upgrade option was disabled.",
        "false_1": "Only Supplier Registration templates support automatic upgrades.",
        "false_2": "The project was created before the template was published.",
        "false_3": "You must edit the Team Member Rules file directly in the active project."
    },
    {
        "question": "Your customer is loading a large group of legacy suppliers as part of their implementation. They want to use the mass registration invitations option but have concerns with sending all of the invitations at once. Which option do you recommend?",
        "correct_answer": "Import all legacy suppliers, then upload waves to send the invitations to multiple subsets of the suppliers.",
        "false_1": "Use the manual single-supplier invitation process for all legacy suppliers.",
        "false_2": "Create multiple, smaller mass invitation projects to handle the subsets.",
        "false_3": "The mass invitation feature sends all invitations immediately upon import."
    },
    {
        "question": "Which features are included in SAP Ariba Supplier Performance Management?",
        "correct_answer": "Supplier scorecards; Supplier surveys",
        "false_1": "Risk control assessments; Adverse media alerts",
        "false_2": "Contract authoring tools; Clause library",
        "false_3": "Sourcing event creation; Bid optimization"
    },
    {
        "question": "Which group assignment enables mass supplier upload via the SM Administration area?",
        "correct_answer": "SM Ops Admin",
        "false_1": "SM ERP Admin",
        "false_2": "Supplier Request Manager",
        "false_3": "Sensitive Data Access"
    },
    {
        "question": "Your customer approves the disqualification of a supplier for Software, a category that appears under IT Services in the category hierarchy. What additional change occurs for this supplier?",
        "correct_answer": "The supplier’s preferred category status for IT Services is removed.",
        "false_1": "The supplier's registration status is changed to 'Denied'.",
        "false_2": "The supplier is automatically disqualified for all other categories.",
        "false_3": "The supplier's inherent risk score is automatically lowered."
    },
    {
        "question": "Which of the following are characteristics of recurring phases?",
        "correct_answer": "They can be started automatically based on recurrence schedule; They can be triggered manually in between scheduled occurrences.",
        "false_1": "They must use a simple workflow; They are only available in Supplier Registration projects.",
        "false_2": "They do not allow the use of performance scorecards; They can only be scheduled annually.",
        "false_3": "The phase title must be static; They cannot contain any tasks."
    },
    {
        "question": "What is the most frequent schedule on which SAP Ariba will load data into a custom fact table?",
        "correct_answer": "Monthly",
        "false_1": "Daily",
        "false_2": "Weekly",
        "false_3": "Quarterly"
    },
    {
        "question": "Your customer has recently renewed a contract with a supplier. As part of this process the target for their on time delivery KPI has increased to 96%. What should the customer update to reflect this change for future performance reviews?",
        "correct_answer": "The master survey and scorecard in the related Supplier Performance Management project",
        "false_1": "The KPI configuration in the ERP system master data.",
        "false_2": "The supplier's profile data in the Supplier 360 view.",
        "false_3": "The contract workspace document for the renewed contract."
    },
    {
        "question": "Which of the following is a benefit of using template questions in Supplier Performance Management projects?",
        "correct_answer": "Collect data for analytical reports",
        "false_1": "Define the approval workflow for the project",
        "false_2": "Set up the data mapping for ERP integration",
        "false_3": "Control the visibility of folders and documents"
    },
    {
        "question": "Scenario: A procurement manager needs to implement principles of clean core management in the ERP system. What actions should be prioritized?",
        "correct_answer": "Minimizing customizations; Ensuring system flexibility; Reducing adaptation efforts",
        "false_1": "Maximizing the use of custom ABAP code; Centralizing all business logic in the ERP",
        "false_2": "Integrating all legacy systems directly; Avoiding any cloud-based solutions",
        "false_3": "Increasing data redundancy; Delaying all system updates"
    },
    {
        "question": "Scenario: A procurement manager needs to evaluate new suppliers and ensure they meet the company's standards. Which components in SAP Ariba Supplier Lifecycle Management should be utilized?",
        "correct_answer": "Supplier requests; Supplier registration; Supplier qualification",
        "false_1": "Sourcing events; Contract authoring; Spend analysis",
        "false_2": "Risk control assessments; Adverse media monitoring; Risk thresholds",
        "false_3": "Invoice processing; Payment reconciliation; Purchase order creation"
    },
    {
        "question": "Which template type defines assessments for control-based engagement risk projects?",
        "correct_answer": "Modular supplier management questionnaire project templates",
        "false_1": "Supplier Registration project template",
        "false_2": "Supplier Performance Management project template",
        "false_3": "Contract Workspace (Procurement) template"
    },
    {
        "question": "Your customer wants to classify performance tier levels for easy reporting. Which option would you recommend?",
        "correct_answer": "Create a custom field on the Supplier Performance Management project layout.",
        "false_1": "Use the supplier's qualification status as the performance tier.",
        "false_2": "Define the tier level in the ERP system master data.",
        "false_3": "Use a standard field on the supplier's 360 profile."
    },
    {
        "question": "Which actions can you perform in the Preferred area?",
        "correct_answer": "View current preferred category status information; Request a preferred category status change.",
        "false_1": "Approve a supplier's qualification for a category; Disqualify a supplier.",
        "false_2": "Update the supplier's registration details; Change the supplier's ID.",
        "false_3": "Set the supplier's inherent risk score; Monitor risk alerts."
    },
    {
        "question": "Scenario: A procurement manager wants to ensure seamless integration with the company's ERP system. What activities should be prioritized in SAP Ariba Supplier Lifecycle Management?",
        "correct_answer": "Increased efficiency; Consistency across projects",
        "false_1": "Higher risk exposure; Decentralized data management",
        "false_2": "Manual data entry; Reduced data visibility",
        "false_3": "Complex customizations; Delayed system updates"
    },
    {
        "question": "What is the primary goal of managing a clean core in ERP systems?",
        "correct_answer": "To maximize business process agility",
        "false_1": "To increase system complexity and customizations",
        "false_2": "To minimize the use of cloud solutions",
        "false_3": "To centralize all transactional data in the ERP"
    },
    {
        "question": "Which project type can be upgraded to the latest version of the template?",
        "correct_answer": "Supplier registration template; Modular supplier management questionnaire template",
        "false_1": "Sourcing Request template; Contract Workspace (Procurement) template",
        "false_2": "Supplier Request template; Supplier Audit template",
        "false_3": "Risk Assessment template; Performance Survey template"
    },
    {
        "question": "Your customer wants a question to be answered by an enterprise user as part of their registration process. Which option do you recommend?",
        "correct_answer": "Internal questionnaire",
        "false_1": "External questionnaire",
        "false_2": "Supplier performance survey",
        "false_3": "Risk control assessment"
    },
    {
        "question": "Your customer wants to include a question as a search filter. Which option do you use when setting up the question?",
        "correct_answer": "Search term",
        "false_1": "Validation Pattern",
        "false_2": "Read-only",
        "false_3": "Calculated value"
    },
    {
        "question": "Which activities are involved in planning for integration and synchronization with ERPs in SAP Ariba Supplier Lifecycle Management?",
        "correct_answer": "Configuring data mappings; Setting up data synchronization schedules",
        "false_1": "Creating performance scorecards; Running supplier surveys",
        "false_2": "Defining risk categories; Monitoring third-party risk alerts",
        "false_3": "Designing the supplier registration form layout"
    },
    {
        "question": "Your customer needs to evaluate supplier performance. Which items are required to collect the supplier's performance data?",
        "correct_answer": "At least one KPI; A scorecard",
        "false_1": "A risk mitigation plan; An adverse media alert",
        "false_2": "An active contract; An approved invoice",
        "false_3": "A registered status; A Supplier Request"
    },
    {
        "question": "Which options are available to populate scorecard KPIs with data outside of a survey?",
        "correct_answer": "Manually enter the KPI value; Map KPIs to an existing analytical report",
        "false_1": "Automatically pull data from the supplier's registration questionnaire.",
        "false_2": "Use a simple approval rule to set the value.",
        "false_3": "The KPI value can only be populated via a survey response."
    },
    {
        "question": "Scenario: A procurement manager needs to create a new project using an existing workspace template. What steps should be taken in SAP Ariba Supplier Performance Management?",
        "correct_answer": "Select the appropriate workspace template; Define performance metrics",
        "false_1": "Automate invoice processing; Generate purchase orders",
        "false_2": "Configure risk thresholds; Monitor adverse media alerts",
        "false_3": "Upload the user matrix file; Set up data mappings to the ERP"
    },
    {
        "question": "Scenario: A procurement manager wants to ensure comprehensive risk management for suppliers. What features in SAP Ariba Supplier Risk Administration should be utilized?",
        "correct_answer": "Risk assessment module; Risk categories; Risk thresholds",
        "false_1": "Performance scorecards; Supplier surveys; Performance metrics",
        "false_2": "Supplier registration form; Contact management; Supplier ID management",
        "false_3": "Sourcing event creation; Bid analysis; Savings tracking"
    },
    {
        "question": "Which actions are available to decision makers when all assessments for a control are approved?",
        "correct_answer": "Mark the control as effective or ineffective; Create issues related to the control.",
        "false_1": "Automatically change the supplier's qualification status to 'Qualified'.",
        "false_2": "Approve a pending contract workspace; Run a new sourcing event.",
        "false_3": "Set a new risk exposure threshold for the supplier."
    },
    {
        "question": "Scenario: A company wants to ensure consistency across all supplier performance projects. How can workspace templates be utilized in SAP Ariba Supplier Lifecycle Management?",
        "correct_answer": "Customize templates for different project types; Standardize project tasks; Include performance evaluation criteria",
        "false_1": "To manage supplier data synchronization with the ERP; To define risk control definitions.",
        "false_2": "To store all supplier bank account details; To set sensitive data mask patterns.",
        "false_3": "To track third-party risk alerts; To monitor adverse media."
    },
    {
        "question": "What functionalities are provided by managing user groups in SAP Ariba Supplier Lifecycle Management?",
        "correct_answer": "Defining access controls; Assigning user roles",
        "false_1": "Calculating performance scores; Creating analytical reports",
        "false_2": "Defining data mappings to the ERP; Setting up data synchronization schedules",
        "false_3": "Monitoring risk dashboards; Setting risk exposure thresholds"
    },
    {
        "question": "While reviewing a supplier organization, your customer notices that the category status area is missing. Why is this the case?",
        "correct_answer": "The category status is only visible for suppliers that are qualified for at least one commodity category.",
        "false_1": "The supplier has not completed their registration questionnaire.",
        "false_2": "The user does not have the 'Supplier Request Manager' group.",
        "false_3": "The supplier has a high-risk exposure score."
    },
    {
        "question": "Which of the following benefits are offered by both SAP Ariba Supplier Information and Performance Management and SAP Ariba Supplier Lifecycle and Performance?",
        "correct_answer": "Supplier self-service portal; Template-based supplier management processes",
        "false_1": "Unified vendor model; Integrated risk management",
        "false_2": "Clean core implementation support; Cloud Integration Gateway (CIG) only",
        "false_3": "Modular questionnaire support; Preferred supplier management"
    },
    {
        "question": "Which users can create engagement-level issues for control-based engagement risk assessment projects?",
        "correct_answer": "The engagement requesters; Members of the Supplier Risk Engagement Governance Analyst group",
        "false_1": "The SM ERP Admin; The Sensitive Data Access user",
        "false_2": "The supplier contact; The supplier request manager",
        "false_3": "The performance review participant; The contract administrator"
    },
    {
        "question": "Which options does SAP Ariba Supplier Lifecycle and Performance support for processing supplier registrations?",
        "correct_answer": "Internal users manually invite a supplier contact to register after the supplier request is approved; Internal users complete the registration on behalf of a supplier; Administrators send mass invitations to groups of suppliers.",
        "false_1": "Only the supplier can initiate and complete their own registration.",
        "false_2": "Registration is always a simple workflow that only requires a single internal approval.",
        "false_3": "Mass invitations can only be sent to suppliers already in the ERP system."
    },
]

# =========================================================================
# 2. CÓDIGO DE STREAMLIT (SIN CAMBIOS)
# =========================================================================

SCORE_FILE = "score_history.json"
# Asegura que haya suficientes preguntas para el examen de 80.
NUM_QUESTIONS_DESIRED = min(80, len(quiz_questions)) 


# --- Lógica de Persistencia (Igual que antes) ---

def _load_scores():
    """Carga el historial de puntuaciones desde el archivo JSON."""
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def _save_scores(history):
    """Guarda el historial de puntuaciones en el archivo JSON."""
    with open(SCORE_FILE, 'w') as f:
        json.dump(history, f, indent=4)

# --- Funciones de Lógica de la Aplicación ---

def initialize_session():
    """Inicializa el estado de Streamlit si es la primera vez."""
    if 'quiz_started' not in st.session_state:
        st.session_state.quiz_started = False
        st.session_state.current_question_index = 0
        st.session_state.current_score = 0
        st.session_state.selected_questions = []
        st.session_state.history = _load_scores()
        st.session_state.show_history = False
        st.session_state.show_results = False

def start_new_attempt():
    """Selecciona N preguntas al azar e inicializa el score."""
    total_available = len(quiz_questions)
    
    if total_available < NUM_QUESTIONS_DESIRED:
        st.error(f"Error: Only {total_available} questions available. Cannot start a {NUM_QUESTIONS_DESIRED} question quiz.")
        return

    st.session_state.current_score = 0
    st.session_state.current_question_index = 0
    st.session_state.selected_questions = random.sample(quiz_questions, NUM_QUESTIONS_DESIRED)
    st.session_state.quiz_started = True
    st.session_state.show_results = False
    st.session_state.user_answer = None # Reiniciar la respuesta del radio
    
    # Reiniciar claves de opciones para un nuevo intento
    for key in list(st.session_state.keys()):
        if key.startswith("q_"):
            del st.session_state[key]
            
    st.rerun()

def check_answer():
    """Verifica la respuesta seleccionada y pasa a la siguiente pregunta."""
    # Se utiliza la clave única 'user_answer' que guarda la selección del radio
    selected_answer = st.session_state.get('user_answer')
    
    if selected_answer is None:
        st.warning("Please select an answer before proceeding.")
        return

    q_data = st.session_state.selected_questions[st.session_state.current_question_index]

    # Comprobar la respuesta
    if selected_answer == q_data["correct_answer"]:
        st.session_state.current_score += 1
    
    # Mover a la siguiente pregunta
    st.session_state.current_question_index += 1
    st.session_state.user_answer = None # Reiniciar la selección para la próxima pregunta
    st.rerun()

def end_attempt():
    """Finaliza el intento, guarda el score y muestra el resultado final."""
    total = len(st.session_state.selected_questions)
    percentage = (st.session_state.current_score / total) * 100 if total > 0 else 0

    # 1. Registrar el score
    record = {
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'score': st.session_state.current_score,
        'total': total,
        'percentage': round(percentage, 2)
    }
    st.session_state.history.append(record)
    _save_scores(st.session_state.history)

    # 2. Actualizar estado y mostrar resultados
    st.session_state.quiz_started = False
    st.session_state.show_results = True
    st.rerun()

def show_quiz_page():
    """Muestra la interfaz del quiz pregunta por pregunta, con clave única para las opciones (solución al bug)."""
    
    current_index = st.session_state.current_question_index
    total = len(st.session_state.selected_questions)

    if current_index >= total:
        end_attempt()
        return

    q_data = st.session_state.selected_questions[current_index]
    question_num = current_index + 1
    
    # -------------------- SOLUCIÓN AL BUG DE MOVIMIENTO --------------------
    question_key = f"q_{current_index}" 
    
    # Si la lista de opciones para esta pregunta no existe en el estado de sesión, la creamos y la guardamos.
    if question_key not in st.session_state:
        options_list = [
            q_data["correct_answer"],
            q_data["false_1"],
            q_data["false_2"],
            q_data["false_3"]
        ]
        random.shuffle(options_list)
        st.session_state[question_key] = options_list
    
    # Obtenemos la lista de opciones (ya mezcladas y guardadas)
    options_to_display = st.session_state[question_key]
    # -------------------- FIN SOLUCIÓN AL BUG --------------------


    st.subheader(f"Question {question_num}/{total}")
    st.markdown(f"**Score: {st.session_state.current_score}**")
    st.markdown("---")
    
    st.info(f"**{q_data['question']}**")

    # Muestra los RadioButtons de Streamlit
    st.radio(
        "Select your answer:",
        options_to_display, 
        key='user_answer', 
        index=None, 
    )

    # Botón de Siguiente Pregunta
    st.button("Next Question", on_click=check_answer, key="next_q_btn")


def show_results_page():
    """Muestra la página de resultados y el historial."""
    latest_record = st.session_state.history[-1]
    
    st.header("✅ Quiz Complete!")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    col1.metric("Final Score", f"{latest_record['score']} / {latest_record['total']}")
    col2.metric("Percentage", f"{latest_record['percentage']:.2f}%")

    st.markdown("---")
    
    if st.button("Start New Attempt", key='new_attempt_btn_results'):
        start_new_attempt()

    if st.button("View Score History", key='view_history_btn_results'):
        st.session_state.show_history = True
        st.rerun()


def show_history_page():
    """Muestra el historial completo en la misma página."""
    st.header("📋 Score History")
    st.markdown("---")
    
    if not st.session_state.history:
        st.warning("No attempts recorded yet.")
    else:
        # Crea una tabla con el historial
        history_data = [
            (i + 1, record['date'], f"{record['score']}/{record['total']}", f"{record['percentage']:.2f}%")
            for i, record in enumerate(st.session_state.history)
        ]
        
        st.table(history_data)

    if st.button("Go Back to Home", key='back_from_history'):
        st.session_state.show_history = False
        st.rerun()


# --- Aplicación Principal (Main App) ---

def main_app():
    initialize_session()
    
    st.title("SAP Ariba SLP Certification Simulator")
    st.sidebar.header("Quiz Menu")
    
    if st.session_state.show_history:
        show_history_page()
    elif st.session_state.quiz_started:
        show_quiz_page()
    elif st.session_state.show_results:
        show_results_page()
    else:
        st.markdown(f"Welcome! This quiz will test you on **{NUM_QUESTIONS_DESIRED} randomly selected questions** from your set of {len(quiz_questions)}.")
        
        st.sidebar.button("Start Quiz", on_click=start_new_attempt, key='start_q_sidebar')
        st.sidebar.button("View History", on_click=lambda: setattr(st.session_state, 'show_history', True) or st.rerun(), key='view_h_sidebar')
        
        if st.session_state.history:
             st.markdown("---")
             st.subheader("Last Attempt")
             latest = st.session_state.history[-1]
             st.write(f"Date: {latest['date']}")
             st.write(f"Score: **{latest['score']} / {latest['total']}** ({latest['percentage']:.2f}%)")


if __name__ == '__main__':
    main_app()