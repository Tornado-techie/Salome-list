# food_safety_audit_tool.py

def get_audit_info():
    print("Welcome to the Food Safety Audit Tool!\n")
    company = input("Enter the company name: ")
    date = input("Enter the audit date (YYYY-MM-DD): ")
    auditor = input("Enter auditor's name: ")
    return {"Company": company, "Date": date, "Auditor": auditor}


def ask_question(section_title, question_text):
    print(f"\n--- {section_title} ---")
    print(question_text)
    compliant = input("Is this compliant? (Yes/No): ")
    severity = input("Severity if not compliant? (Crit/Maj/Min/IMP or leave blank): ")
    observation = input("Any observations? (Optional): ")
    return {
        "Question": question_text,
        "Compliant": compliant,
        "Severity": severity,
        "Observation": observation
    }


def save_audit_results(audit_info, results, filename="audit_results.txt"):
    with open(filename, "w") as f:
        f.write(f"Company: {audit_info['Company']}\n")
        f.write(f"Date: {audit_info['Date']}\n")
        f.write(f"Auditor: {audit_info['Auditor']}\n\n")
        f.write("Audit Results:\n")
        for r in results:
            f.write(f"\n{r['Question']}\n")
            f.write(f"Compliant: {r['Compliant']}\n")
            f.write(f"Severity: {r['Severity']}\n")
            f.write(f"Observation: {r['Observation']}\n")


def main():
    audit_info = get_audit_info()

    checklist = checklist = [
    ("1.1 Pre-Audit Changes", "Have there been any changes to the food safety plan, personnel, processes or packaging?"),
    ("2.1 Responsible Person", "Is there at least one person responsible for the development and maintenance of food safety systems?"),
    ("2.2 HACCP Team", "Is the HACCP system developed and reviewed by a multidisciplinary team with adequate training and experience?"),
    ("2.3 External Consultants", "If external expertise was used, are credentials shown and is day-to-day management still by the company?"),
    ("3.1 Food Safety Policy", "Is the company's product safety policy defined and does it include obligations for safe and legal products?"),
    ("3.2 Quality Policy", "Does the company have a documented quality policy or mission statement?"),
    ("3.3 Quality System", "Is there a documented quality system in place that includes HACCP documentation?"),
    ("3.4 Accreditation", "Is the quality system accredited and by whom?"),
    ("3.5 Hazard Audit Tables", "Do the hazard audit tables reflect product risks?"),
    ("3.6 Complaints Handling", "Is there a documented customer complaints handling procedure?"),
    ("3.7 Recall Procedure", "Is there a documented product recall procedure?"),
    ("4.1 HACCP Principles", "Is the food safety plan based on Codex HACCP principles and does it address all key hazards?"),
    ("4.2 Scope of HACCP", "Does the food safety plan describe the full process from paddock to plate?"),
    ("4.3 Coverage", "Does the food safety plan include all products and processes?"),
    ("4.4 Flow Diagrams", "Does the plan include an appropriate flow diagram of the process?"),
    ("4.5 HACCP Detail", "Does the plan establish CCPs, limits, monitoring, corrective actions, validation, verification, and record keeping?"),
    ("4.6 Risk Assessment", "Does the HACCP study include analysis of likely hazards and severity?"),
    ("4.7 Prerequisite Programs", "Are GMP, allergen control, and other prerequisite programs referenced in documentation?"),
    ("5.1 Raw Materials", "Does the plan include raw materials, packaging, and product specifications?"),
    ("5.2 Specification Reviews", "Are specifications regularly reviewed to ensure adequacy?"),
    ("5.3 Product Characteristics", "Are product characteristics defined, including safety and traceability aspects?"),
    ("5.4 Usage Characteristics", "Are product usage characteristics defined including storage, target group, and labeling?"),
    ("6.1 Flow Diagram Validation", "Are flow diagrams validated and include all key steps like delays, storage, and rework?"),
    ("6.2 Layout Considerations", "Are production layouts documented to address contamination and regulatory needs?"),
    ("6.3 CCP Documentation", "Are monitoring responsibility, limits, actions, and verifications for CCPs defined?"),
    ("6.4 Corrective Actions", "Are food safety incidents documented, investigated, and corrected with feedback and traceability?"),
    ("6.5 Non-conforming Product", "Is identification and disposition of non-conforming products handled under documented procedures?"),
    ("7.1 Verification Schedule", "Does a verification schedule exist with frequency, responsibility, and records defined?"),
    ("7.2 Verification Evidence", "Is there sufficient evidence of implementation of the verification schedule?"),
    ("7.3 Internal Audits", "Are internal audits conducted by independent personnel?"),
    ("7.4 Management Review", "Is there evidence of management reviews and follow-up on deviations?"),
    ("7.5 Regulatory Verification", "Is there a system to ensure compliance with applicable food regulations?"),
    ("8.1 Validation Data", "Does the company have validation data to support safety and compliance claims?"),
    ("9.1 Traceability System", "Can the traceability system identify product lots and raw material batches?"),
    ("9.2 Record Retention", "Are traceability records kept for at least two years?"),
    ("9.3 Recall Procedure", "Is there a documented product recall procedure?"),
    ("9.4 Mock Recalls", "Is the recall system tested periodically with a mock recall?"),
    ("9.5 Traceability Test", "Was a traceability exercise done during the audit and how long did it take?"),
    ("9.6 Supplier Program", "Is there an approved supplier program in place?"),
    ("10.1 Incoming Material Hazards", "Are incoming materials assessed for food safety hazards?"),
    ("10.2 Raw Material Risk", "Does the risk assessment inform the incoming inspection and testing plan?"),
    ("10.3 Goods Inspection", "Are all received goods inspected as per inspection plans?"),
    ("10.4 Supplier Non-Conformance", "Are supplier issues documented and addressed with corrective action?"),
    ("10.5 Supplier Approval", "Are there procedures for approval and removal of suppliers including emergencies?")
]

    results = []
    for section_title, question_text in checklist:
        result = ask_question(section_title, question_text)
        results.append(result)

    save_audit_results(audit_info, results)
    print("\nAudit complete! Results saved to 'audit_results.txt'.")


if __name__ == "__main__":
    main()


