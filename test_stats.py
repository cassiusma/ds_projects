from summary_stats import summary_stats

def test_mean():
    result = summary_stats([2, 4, 6])
    assert result['mean'] == 4.0

def test_median_odd():
    result = summary_stats([1, 2, 3])
    assert result['median'] == 2

def test_median_even():
    result = summary_stats([1, 2, 3, 4])
    assert result['median'] == 2.5

def test_variance():
    result = summary_stats([2, 4, 6])
    assert result['variance'] == 4.0