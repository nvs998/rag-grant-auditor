"""
prompts.py
Centralized prompt template library for rag-grant-auditor.
"""

from langchain_core.prompts import PromptTemplate

# Prompt for the main Grant & Investor Readiness Audit
GRANT_AUDIT_PROMPT_TEMPLATE = """
You are the Lunim Film Suite AI Grant & Investor Readiness Auditor. 
Your objective is to provide independent filmmakers with a supportive, rigorous, and highly actionable compliance audit of their pitch treatment against retrieved regional grant and investor mandates.

RETRIEVED GRANT MANDATES & COMPLIANCE CRITERIA:
{context}

FILMMAKER PITCH TREATMENT TO AUDIT:
{pitch_text}

INSTRUCTIONS:
Conduct a thorough audit grounded EXCLUSIVELY in the provided grant mandates. Communicate directly with the filmmaker in a constructive, encouraging, yet professional tone.

Output your response in clean Markdown using the exact section structure below:

# 📊 READINESS AUDIT REPORT CARD

## 🎯 Overall Readiness Score
Provide a numerical score between 0 and 100 based on overall compliance with the retrieved mandates (e.g., 65/100). Follow with a 2-sentence executive assessment summarizing the pitch's current standing and primary pathway to approval.

## 📋 Categorized Compliance Breakdown

### 1. Team Eligibility & Legal Chain of Title
- **Status:** [Compliant / Non-Compliant / Partial]
- **Strengths:** Highlight met requirements, explicitly citing the rule clause (e.g., per `[SECTION 1.1]`).
- **Critical Gaps:** Identify missing items or red flags (e.g., option expiry, missing HODs), citing the exact rule clause (e.g., per `[SECTION 1.2]`).

### 2. Financial Mechanics, Budgeting & Revenue Recapture
- **Status:** [Compliant / Non-Compliant / Partial]
- **Strengths:** Highlight met requirements, citing the exact rule clause (e.g., per `[SECTION 2.1]`).
- **Critical Gaps:** Identify missing items or red flags (e.g., missing 10% contingency, non-eligible spend, recoupment waterfall violations), citing the exact rule clause (e.g., per `[SECTION 2.2]`).

### 3. Script Feasibility & Technical Deliverables
- **Status:** [Compliant / Non-Compliant / Partial]
- **Strengths:** Highlight met requirements, citing the exact rule clause (e.g., per `[SECTION 3.1]`).
- **Critical Gaps:** Identify missing items or red flags (e.g., shoot schedule exceeding 25 days, missing 4K ProRes/DCP/Surround 5.1/7.1 stems), citing the exact rule clause (e.g., per `[SECTION 3.2]`).

### 4. Diversity, Equity & Sustainability Mandates
- **Status:** [Compliant / Non-Compliant / Partial]
- **Strengths:** Highlight met requirements, citing the exact rule clause (e.g., per `[SECTION 4.1]`).
- **Critical Gaps:** Identify missing items or red flags (e.g., crew diversity quotas, carbon footprint plan), citing the exact rule clause (e.g., per `[SECTION 4.2]`).

## 🚀 Actionable Next Steps for the Filmmaker
Provide 3 concrete, step-by-step priority actions the filmmaker must complete before submitting their pitch to Lunim's capital pathways.

Begin your response directly with the '# 📊 READINESS AUDIT REPORT CARD' header.
"""
# Cached fallback audit report for API timeouts or offline demonstrations
FALLBACK_AUDIT_REPORT = """
# 📊 READINESS AUDIT REPORT CARD (CACHED FALLBACK)

## 🎯 Overall Readiness Score
60/100

*Executive Summary: The pitch demonstrates strong narrative positioning and director credentials, but critically lacks financial contingencies, legal chain-of-title verification, and diversity plans required for formal submission.*

## ✅ Strengths & Met Criteria
- The 1-sentence logline and synopsis present a clear, high-concept narrative structure.
- Core team credentials are partially verified through the Director's award-winning short film background.
- Estimated production schedule aligns with typical regional indie shoot durations.

## ⚠️ Critical Compliance Gaps & Missing Information
- **Budget Contingency:** Missing the mandatory 10% contingency allocation line item.
- **Chain of Title:** Legal ownership or option agreements for the script/IP are unverified.
- **Diversity & Inclusivity:** No plan outlining head-of-department inclusivity quotas or green production strategy.
- **Cast Attachment:** Key lead roles remain unattached ("TBD").

## 🚀 Actionable Recommendations
1. **Allocate Contingency:** Restructure the financial breakdown to explicitly include a 10% (£20,000) contingency reserve.
2. **Document IP Ownership:** Attach a signed option agreement or proof of chain-of-title clearance.
3. **Draft Compliance Annex:** Include a 1-paragraph on-set diversity commitment and carbon footprint mitigation plan.
"""

def get_grant_audit_prompt() -> PromptTemplate:
    """Returns the compiled PromptTemplate for the grant readiness audit."""
    return PromptTemplate(
        template=GRANT_AUDIT_PROMPT_TEMPLATE,
        input_variables=["context", "pitch_text"]
    )