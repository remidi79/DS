"""
Génère un jeu de données synthétique de notation crédit pour un entretien DS finance.

Les données sont volontairement imparfaites :
- valeurs manquantes ;
- lignes dupliquées ;
- valeurs aberrantes ;
- dates non triées ;
- classes déséquilibrées ;
- quelques variables dont la disponibilité doit être vérifiée.

Aucune donnée réelle n'est utilisée.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


RANDOM_SEED = 42
N_ROWS = 20_000
BASE_DIR = Path(__file__).resolve().parent
OUTPUT_PATH = BASE_DIR / "data" / "credit_scoring_interview.csv"


def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-x))


def generate_dataset(n_rows: int = N_ROWS, seed: int = RANDOM_SEED) -> pd.DataFrame:
    rng = np.random.default_rng(seed)

    customer_id = np.arange(100_000, 100_000 + n_rows)

    start_date = np.datetime64("2023-01-01")
    date_offsets = rng.integers(0, 730, size=n_rows)
    application_date = start_date + date_offsets.astype("timedelta64[D]")

    age = np.clip(rng.normal(39, 11, size=n_rows).round(), 18, 75).astype(int)
    employment_years = np.clip(
        rng.gamma(shape=2.0, scale=3.0, size=n_rows), 0, np.maximum(age - 18, 1)
    ).round(1)

    income = rng.lognormal(mean=10.65, sigma=0.45, size=n_rows)
    income = np.clip(income, 12_000, 220_000).round(0)

    loan_amount = rng.lognormal(mean=9.55, sigma=0.55, size=n_rows)
    loan_amount = np.clip(loan_amount, 1_000, 120_000).round(0)

    loan_duration_months = rng.choice(
        [6, 12, 18, 24, 36, 48, 60, 72],
        size=n_rows,
        p=[0.04, 0.13, 0.08, 0.24, 0.22, 0.15, 0.11, 0.03],
    )

    debt_ratio_base = rng.beta(2.0, 7.0, size=n_rows)
    existing_debt = (income * debt_ratio_base * rng.uniform(0.6, 1.5, size=n_rows)).round(0)
    debt_to_income = ((existing_debt + loan_amount / 12) / income).round(4)

    credit_history_months = np.clip(
        ((age - 18) * 12 * rng.uniform(0.2, 0.95, size=n_rows)).round(),
        0,
        650,
    ).astype(int)

    number_of_previous_loans = rng.poisson(
        lam=np.clip(credit_history_months / 80, 0.2, 7.5), size=n_rows
    )
    missed_payments_12m = rng.poisson(
        lam=np.clip(0.15 + debt_to_income * 1.2 + (income < 30_000) * 0.25, 0.05, 2.5),
        size=n_rows,
    )

    region = rng.choice(
        ["Nord", "Sud", "Est", "Ouest", "Centre"],
        size=n_rows,
        p=[0.22, 0.19, 0.18, 0.23, 0.18],
    )
    channel = rng.choice(
        ["agence", "web", "mobile", "courtier"],
        size=n_rows,
        p=[0.28, 0.35, 0.25, 0.12],
    )

    # Génération de la cible : déséquilibrée, avec des facteurs de risque réalistes.
    risk_score = (
        -3.45
        + 1.9 * debt_to_income
        + 0.34 * missed_payments_12m
        + 0.000010 * loan_amount
        - 0.000006 * income
        - 0.018 * employment_years
        - 0.0022 * credit_history_months
        + 0.22 * (channel == "courtier")
        + 0.18 * (channel == "mobile")
        + 0.16 * (region == "Sud")
        + 0.12 * (age < 25)
        + rng.normal(0, 0.42, size=n_rows)
    )
    default_probability = sigmoid(risk_score)
    default_90d = rng.binomial(1, default_probability)

    # Statut de suivi inclus pour discuter la disponibilité des variables.
    collection_status_after_90d = np.where(
        default_90d == 1,
        rng.choice(["a_jour", "recouvrement_amiable", "recouvrement_contentieux"], size=n_rows, p=[0.08, 0.50, 0.42]),
        rng.choice(["a_jour", "recouvrement_amiable", "recouvrement_contentieux"], size=n_rows, p=[0.96, 0.035, 0.005]),
    )

    df = pd.DataFrame(
        {
            "customer_id": customer_id,
            "application_date": application_date.astype("datetime64[D]").astype(str),
            "age": age,
            "income": income,
            "employment_years": employment_years,
            "loan_amount": loan_amount,
            "loan_duration_months": loan_duration_months,
            "existing_debt": existing_debt,
            "debt_to_income": debt_to_income,
            "credit_history_months": credit_history_months,
            "number_of_previous_loans": number_of_previous_loans,
            "missed_payments_12m": missed_payments_12m,
            "region": region,
            "channel": channel,
            "collection_status_after_90d": collection_status_after_90d,
            "default_90d": default_90d,
        }
    )

    # Valeurs manquantes dans des variables numériques et catégorielles.
    for col, frac in {
        "income": 0.018,
        "employment_years": 0.025,
        "existing_debt": 0.012,
        "credit_history_months": 0.015,
        "region": 0.010,
        "channel": 0.008,
    }.items():
        mask = rng.random(n_rows) < frac
        df.loc[mask, col] = np.nan

    # Valeurs aberrantes et enregistrements peu plausibles.
    outlier_idx = rng.choice(df.index, size=90, replace=False)
    df.loc[outlier_idx[:30], "income"] = df.loc[outlier_idx[:30], "income"].fillna(df["income"].median()) * rng.uniform(8, 16, 30)
    df.loc[outlier_idx[30:60], "loan_amount"] = df.loc[outlier_idx[30:60], "loan_amount"] * rng.uniform(5, 10, 30)
    df.loc[outlier_idx[60:75], "age"] = rng.choice([17, 82, 95], size=15)
    df.loc[outlier_idx[75:], "employment_years"] = rng.uniform(45, 62, size=15).round(1)

    # Quelques anomalies de dates et des lignes mélangées pour rendre l'ordre non fiable.
    anomaly_idx = rng.choice(df.index, size=50, replace=False)
    df.loc[anomaly_idx[:25], "application_date"] = "2022-12-15"
    df.loc[anomaly_idx[25:], "application_date"] = "2025-02-01"
    df = df.sample(frac=1.0, random_state=seed).reset_index(drop=True)

    # Lignes entièrement dupliquées et IDs client dupliqués avec des demandes légèrement différentes.
    duplicate_full = df.sample(n=120, random_state=seed + 1)
    duplicate_customer = df.sample(n=80, random_state=seed + 2).copy()
    duplicate_customer["application_date"] = (
        pd.to_datetime(duplicate_customer["application_date"], errors="coerce")
        + pd.to_timedelta(rng.integers(10, 90, size=len(duplicate_customer)), unit="D")
    ).dt.strftime("%Y-%m-%d")
    duplicate_customer["loan_amount"] = (duplicate_customer["loan_amount"] * rng.uniform(0.8, 1.25, len(duplicate_customer))).round(0)

    df = pd.concat([df, duplicate_full, duplicate_customer], ignore_index=True)
    df = df.sample(frac=1.0, random_state=seed + 3).reset_index(drop=True)

    return df


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df = generate_dataset()
    df.to_csv(OUTPUT_PATH, index=False)

    default_rate = df["default_90d"].mean()
    print(f"{len(df):,} lignes générées dans {OUTPUT_PATH}")
    print(f"Taux de défaut : {default_rate:.2%}")
    print("Jeu de données synthétique uniquement. Aucune donnée réelle n'a été utilisée.")


if __name__ == "__main__":
    main()
