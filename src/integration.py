
from pathlib import Path
import pandas as pd

FILES = {
    "carbon": "BOL - Subnational 2 carbon data.csv",
    "tree_cover": "BOL - Subnational 2 tree cover loss.csv",
    "drivers": "BOL - Subnational 2 drivers.csv",
    "primary_drivers": "BOL - Subnational 2 primary drivers.csv",
    "primary_loss": "BOL - Subnational 2 primary loss.csv"
}

KEYS = [
    "country", "subnational1", "subnational2",
    "threshold", "year"
]


def aggregate_drivers(df, output_column):
    """Aggregate driver-attributed forest loss."""
    return (
        df.groupby(KEYS, as_index=False)["tc_loss_ha"]
        .sum()
        .rename(columns={"tc_loss_ha": output_column})
    )


def build_dataset(data_path):
    """Build and validate the integrated forest dataset."""
    data_path = Path(data_path)

    raw = {
        name: pd.read_csv(data_path / filename)
        for name, filename in FILES.items()
    }

    base = (
        raw["tree_cover"]
        .loc[lambda df: df["threshold"].eq(30)]
        .rename(columns={"tc_loss_ha": "tree_loss_ha"})
        .copy()
    )

    sources = {
        "carbon": raw["carbon"].query("threshold == 30").copy(),
        "primary_loss": raw["primary_loss"].copy(),
        "drivers": aggregate_drivers(
            raw["drivers"], "drivers_sum_ha"
        ),
        "primary_drivers": aggregate_drivers(
            raw["primary_drivers"], "primary_drivers_sum_ha"
        )
    }

    result = base

    for name, source in sources.items():
        result = result.merge(
            source,
            on=KEYS,
            how="left",
            validate="one_to_one",
            indicator=True
        )

        result[f"has_{name}"] = result.pop("_merge").eq("both")

    if len(result) != len(base):
        raise ValueError("Unexpected row multiplication")

    if result.duplicated(KEYS).any():
        raise ValueError("Duplicate composite keys")

    if not result.loc[
        result["year"].eq(2001), "primary_tc_loss_ha"
    ].isna().all():
        raise ValueError("Invalid primary loss coverage")

    return result
