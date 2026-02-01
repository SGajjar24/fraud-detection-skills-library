"""
Section 17 Registration Act Compliance Validator

Legal Principle:
Section 17(1)(b) of the Registration Act, 1908 states that documents which purport
to assign, limit, or extinguish any right, title, or interest in immovable property
of value >= Rs.100 MUST be registered to have legal effect.

Section 49 clarifies: Unregistered documents cannot be received as evidence of the
transaction they purport to effect.

Result: Unregistered deed = VOID AB INITIO (invalid from inception)
"""

from typing import Dict, List


# Document types that REQUIRE registration
MANDATORY_REGISTRATION_TYPES = [
    "Sale Deed",
    "Gift Deed",
    "Exchange Deed",
    "Relinquishment Deed",  # Faragati Lekh
    "Partition Deed",
    "Mortgage Deed",
    "Lease Deed (>1 year)"
]


def validate_section_17_compliance(
    document_type: str,
    property_value: float,
    registration_number: str = None,
    is_notarized: bool = False
) -> Dict:
    """
    Validates if a document complies with Section 17 of Registration Act 1908.
    
    Args:
        document_type: Type of legal instrument (e.g., "Sale Deed", "Relinquishment")
        property_value: Transaction/property value in INR
        registration_number: Sub-Registrar office registration ID (None if unregistered)
        is_notarized: Whether document was notarized (insufficient substitute for registration)
        
    Returns:
        {
            "compliant": bool,
            "legal_status": "VALID" | "VOID_AB_INITIO",
            "section": str,
            "explanation": str
        }
        
    Example:
        >>> validate_section_17_compliance(
        ...     document_type="Relinquishment Deed",
        ...     property_value=500000,
        ...     registration_number=None,
        ...     is_notarized=True
        ... )
        {
            "compliant": False,
            "legal_status": "VOID_AB_INITIO",
            "section": "Registration Act 1908, Section 17(1)(b) + Section 49"
        }
    """
    
    requires_registration = document_type in MANDATORY_REGISTRATION_TYPES
    exceeds_threshold = property_value >= 100
    
    if requires_registration and exceeds_threshold:
        if not registration_number:
            explanation = (
                f"'{document_type}' of value Rs.{property_value:,.2f} requires registration "
                f"under Section 17(1)(b). "
            )
            
            if is_notarized:
                explanation += "Notarization does NOT cure the defect. "
            
            explanation += (
                "Per Section 49, this document cannot be received as evidence of any "
                "transaction affecting immovable property. STATUS: VOID AB INITIO."
            )
            
            return {
                "compliant": False,
                "legal_status": "VOID_AB_INITIO",
                "section": "Registration Act, 1908, Section 17(1)(b) + Section 49",
                "explanation": explanation,
                "can_be_evidence": False
            }
    
    return {
        "compliant": True,
        "legal_status": "VALID",
        "section": "N/A",
        "explanation": f"'{document_type}' complies with Registration Act requirements.",
        "can_be_evidence": True
    }


if __name__ == "__main__":
    result = validate_section_17_compliance(
        document_type="Relinquishment Deed",
        property_value=750000,
        registration_number=None,
        is_notarized=True
    )
    
    print("=== Section 17 Compliance Check ===")
    print(f"Legal Status: {result['legal_status']}")
    print(f"Compliant: {result['compliant']}")
    print(f"Statute: {result['section']}")
    print(f"Explanation: {result['explanation']}")
