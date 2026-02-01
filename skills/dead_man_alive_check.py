"""
Dead Man Alive Check - Temporal Fraud Detection

Legal Principle:
Under Section 68 of the Indian Evidence Act, 1872, if a signatory was deceased
at the time of document execution, the document is presumed fraudulent unless
proven otherwise.

Use Cases:
- Property sale deeds signed posthumously
- Wills executed after testator's death
- Power of Attorney granted after death
"""

from datetime import datetime, timedelta
from typing import Dict, Optional


def detect_posthumous_signatures(
    signatory: str,
    death_date: str,
    document_date: str,
    grace_period_days: int = 7
) -> Dict:
    """
    Detects if a document was signed after the signatory's official death date.
    
    Args:
        signatory: Full name of the deceased person
        death_date: Official death date in YYYY-MM-DD format
        document_date: Document execution date in YYYY-MM-DD format
        grace_period_days: Allow N days for bureaucratic processing delays (default: 7)
        
    Returns:
        {
            "signatory": str,
            "is_fraudulent": bool,
            "days_after_death": int,
            "legal_risk": "LOW" | "MEDIUM" | "HIGH",
            "statute": str,
            "recommendation": str
        }
        
    Example:
        >>> detect_posthumous_signatures(
        ...     signatory="Goradhanbhai Suthar",
        ...     death_date="2016-03-15",
        ...     document_date="2025-01-10"
        ... )
        {
            "is_fraudulent": True,
            "days_after_death": 3259,
            "legal_risk": "HIGH",
            "statute": "Indian Evidence Act Section 68"
        }
    """
    try:
        death = datetime.strptime(death_date, "%Y-%m-%d")
        execution = datetime.strptime(document_date, "%Y-%m-%d")
    except ValueError as e:
        raise ValueError(f"Invalid date format. Use YYYY-MM-DD: {e}")
    
    days_diff = (execution - death).days
    
    # If document is dated BEFORE death, no fraud
    if days_diff < 0:
        return {
            "signatory": signatory,
            "is_fraudulent": False,
            "days_after_death": 0,
            "legal_risk": "LOW",
            "statute": "N/A",
            "recommendation": "Document executed before death. No temporal fraud detected."
        }
    
    # Allow grace period for legitimate processing delays
    if days_diff <= grace_period_days:
        return {
            "signatory": signatory,
            "is_fraudulent": False,
            "days_after_death": days_diff,
            "legal_risk": "LOW",
            "statute": "N/A",
            "recommendation": f"Within {grace_period_days}-day grace period. Possibly legitimate processing delay."
        }
    
    # Document signed after grace period = FRAUD
    legal_risk = "HIGH" if days_diff > 365 else "MEDIUM"
    
    return {
        "signatory": signatory,
        "is_fraudulent": True,
        "days_after_death": days_diff,
        "legal_risk": legal_risk,
        "statute": "Indian Evidence Act, 1872, Section 68",
        "recommendation": f"Document signed {days_diff} days after death. Strong evidence of forgery. "
                         f"Recommend forensic signature analysis and investigation of beneficiaries."
    }


# Example Case: Real litigation scenario
if __name__ == "__main__":
    result = detect_posthumous_signatures(
        signatory="Goradhanbhai Suthar",
        death_date="2016-03-15",
        document_date="2025-01-10"
    )
    
    print("=== Dead Man Alive Fraud Detection ===")
    print(f"Signatory: {result['signatory']}")
    print(f"Fraudulent: {result['is_fraudulent']}")
    print(f"Days After Death: {result['days_after_death']}")
    print(f"Legal Risk: {result['legal_risk']}")
    print(f"Statute: {result['statute']}")
    print(f"Recommendation: {result['recommendation']}")
