import io
import unittest
from contextlib import redirect_stdout

import films


class TestFilmsAnalyzer(unittest.TestCase):
    def test_ac1_is_rating_above_5(self) -> None:
        buf = io.StringIO()
        with redirect_stdout(buf):
            res_low = films.isRatingAbove5("AlphaJet")
            res_high = films.isRatingAbove5("Joking muck")
        self.assertFalse(res_low)
        self.assertTrue(res_high)
        self.assertEqual(buf.getvalue().splitlines(), ["False", "True"])

    def test_ac2_sublist_rating_above_5(self) -> None:
        result = films.getSublistOfRatingAbove5(films.movies)
        self.assertEqual(len(result), 11)
        self.assertTrue(all(m["imdb"] > 5.5 for m in result))

    def test_ac3_sublist_category_romance(self) -> None:
        result = films.getSublistOfCategory(films.movies, "Romance")
        names = [m["name"] for m in result]
        self.assertEqual(names, ["The Choice", "Colonia", "Love", "Bride Wars", "We Two"])

    def test_ac4_average_in_category_thriller(self) -> None:
        avg = films.calculateAverageInCategory(films.movies, "Thriller")
        self.assertAlmostEqual(avg, 5.6)

    def test_r01_custom_sublist_average_ignores_global_movies(self) -> None:
        custom = [
            {"name": "Custom A", "imdb": 10.0, "category": "Sci-Fi"},
            {"name": "Custom B", "imdb": 8.0, "category": "Sci-Fi"},
        ]
        self.assertAlmostEqual(films.calculateAverage(custom), 9.0)
        self.assertAlmostEqual(films.calculateAverageInCategory(custom, "Sci-Fi"), 9.0)

    def test_r02_empty_list_and_unknown_category_no_zero_division(self) -> None:
        self.assertEqual(films.calculateAverage([]), 0.0)
        self.assertEqual(films.calculateAverageInCategory(films.movies, "NonExistent"), 0.0)


if __name__ == "__main__":
    unittest.main()