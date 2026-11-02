
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from integration import build_dataset, KEYS


class TestForestIntegration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        data_dir = (
            ROOT / "data" / "raw"
            if (ROOT / "data" / "raw").exists()
            else ROOT
        )
        cls.df = build_dataset(data_dir)

    def test_expected_shape(self):
        self.assertEqual(self.df.shape, (2800, 23))

    def test_unique_keys(self):
        self.assertEqual(
            int(self.df.duplicated(KEYS).sum()), 0
        )

    def test_years_and_threshold(self):
        self.assertTrue(
            self.df["year"].between(2001, 2025).all()
        )
        self.assertTrue(
            self.df["threshold"].eq(30).all()
        )

    def test_primary_loss_2001(self):
        values = self.df.loc[
            self.df["year"] == 2001,
            "primary_tc_loss_ha"
        ]
        self.assertTrue(values.isna().all())

    def test_source_coverage(self):
        expected = {
            "carbon": 2800,
            "primary_loss": 1296,
            "drivers": 1636,
            "primary_drivers": 1272
        }

        for name, count in expected.items():
            with self.subTest(source=name):
                self.assertEqual(
                    int(self.df[f"has_{name}"].sum()),
                    count
                )


if __name__ == "__main__":
    unittest.main()
