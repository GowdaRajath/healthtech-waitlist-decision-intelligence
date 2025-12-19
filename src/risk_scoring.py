import pandas as pd


def calculate_risk_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate an explainable risk score based on:
    - Waiting time
    - Referral priority
    - Historical cancellations

    This function is intentionally transparent and deterministic
    to support governance and clinical oversight.
    """

    df = df.copy()

    # Normalised wait time component
    df["wait_risk"] = df["wait_days"] / df["wait_days"].max()

    # Priority contribution
    priority_weight = {
        "Routine": 0.1,
        "Urgent": 0.6,
        "Two-Week Wait": 1.0
    }
    df["priority_risk"] = df["priority_level"].map(priority_weight)

    # Cancellation contribution
    df["cancellation_risk"] = (
        df["previous_cancellations"] /
        (df["previous_cancellations"].max() + 1)
    )

    # Final weighted risk score
    df["risk_score"] = (
        df["wait_risk"] * 0.6 +
        df["priority_risk"] * 0.2 +
        df["cancellation_risk"] * 0.2
    ).round(3)

    return df


def assign_risk_band(df: pd.DataFrame) -> pd.DataFrame:
    """
    Assign risk bands for interpretability.
    """

    df = df.copy()

    df["risk_band"] = pd.cut(
        df["risk_score"],
        bins=[0.0, 0.3, 0.6, 0.8, 1.0],
        labels=["Low", "Moderate", "High", "Critical"]
    )

    return df


def recommend_review(df: pd.DataFrame) -> pd.DataFrame:
    """
    Recommend review for high and critical risk cases.
    """

    df = df.copy()

    df["review_recommended"] = df["risk_band"].isin(
        ["High", "Critical"]
    )

    return df
