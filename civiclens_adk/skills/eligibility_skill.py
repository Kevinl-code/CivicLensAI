from ..tools.eligibility_tool import check_eligibility

def eligibility_skill(text: str):
    """
    Reusable eligibility extraction skill.
    """

    return check_eligibility(text)