"""
Statistics Module
Contains statistical calculations, probability functions, and data analysis tools.
"""
import numpy as np
from typing import List, Union, Tuple
from scipy import stats

class Statistics:
    @staticmethod
    def descriptive_stats(data: List[float]) -> dict:
        """
        Calculate comprehensive descriptive statistics for a dataset
        Args:
            data: List of numerical values
        Returns:
            Dictionary containing various statistical measures
        """
        return {
            'mean': np.mean(data),
            'median': np.median(data),
            'mode': stats.mode(data, keepdims=True)[0][0],
            'std_dev': np.std(data),
            'variance': np.var(data),
            'min': np.min(data),
            'max': np.max(data),
            'range': np.max(data) - np.min(data),
            'q1': np.percentile(data, 25),
            'q3': np.percentile(data, 75),
            'iqr': np.percentile(data, 75) - np.percentile(data, 25),
            'skewness': stats.skew(data),
            'kurtosis': stats.kurtosis(data)
        }

    @staticmethod
    def correlation_analysis(x: List[float], y: List[float]) -> dict:
        """
        Perform correlation analysis between two variables
        Args:
            x: First dataset
            y: Second dataset
        Returns:
            Dictionary containing correlation coefficients and p-values
        """
        pearson_corr, pearson_p = stats.pearsonr(x, y)
        spearman_corr, spearman_p = stats.spearmanr(x, y)
        
        return {
            'pearson_correlation': pearson_corr,
            'pearson_p_value': pearson_p,
            'spearman_correlation': spearman_corr,
            'spearman_p_value': spearman_p
        }

    @staticmethod
    def hypothesis_testing(sample1: List[float], sample2: List[float] = None, 
                         test_type: str = 't_test', alpha: float = 0.05) -> dict:
        """
        Perform various statistical hypothesis tests
        Args:
            sample1: First sample data
            sample2: Second sample data (optional)
            test_type: Type of test ('t_test', 'wilcoxon', 'mann_whitney')
            alpha: Significance level
        Returns:
            Dictionary containing test results
        """
        if test_type == 't_test':
            if sample2 is None:
                # One-sample t-test against mean=0
                t_stat, p_value = stats.ttest_1samp(sample1, 0)
                test_name = "One-sample t-test"
            else:
                # Two-sample t-test
                t_stat, p_value = stats.ttest_ind(sample1, sample2)
                test_name = "Two-sample t-test"
        elif test_type == 'wilcoxon':
            if sample2 is None:
                # Wilcoxon signed-rank test
                t_stat, p_value = stats.wilcoxon(sample1)
                test_name = "Wilcoxon signed-rank test"
            else:
                raise ValueError("Wilcoxon test requires only one sample")
        elif test_type == 'mann_whitney':
            if sample2 is not None:
                # Mann-Whitney U test
                t_stat, p_value = stats.mannwhitneyu(sample1, sample2)
                test_name = "Mann-Whitney U test"
            else:
                raise ValueError("Mann-Whitney U test requires two samples")
        else:
            raise ValueError("Invalid test type")

        return {
            'test_name': test_name,
            'statistic': t_stat,
            'p_value': p_value,
            'significant': p_value < alpha
        }

    @staticmethod
    def probability_distribution(dist_type: str, **params) -> Tuple[np.ndarray, np.ndarray]:
        """
        Generate probability distribution
        Args:
            dist_type: Type of distribution ('normal', 'uniform', 'poisson', etc.)
            **params: Distribution parameters
        Returns:
            Tuple of (x values, probability values)
        """
        if dist_type == 'normal':
            mu = params.get('mu', 0)
            sigma = params.get('sigma', 1)
            x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)
            y = stats.norm.pdf(x, mu, sigma)
        elif dist_type == 'uniform':
            a = params.get('a', 0)
            b = params.get('b', 1)
            x = np.linspace(a - 0.1*(b-a), b + 0.1*(b-a), 100)
            y = stats.uniform.pdf(x, a, b-a)
        elif dist_type == 'poisson':
            mu = params.get('mu', 1)
            x = np.arange(0, mu*3)
            y = stats.poisson.pmf(x, mu)
        else:
            raise ValueError("Unsupported distribution type")
            
        return x, y

    @staticmethod
    def confidence_interval(data: List[float], confidence: float = 0.95) -> Tuple[float, float]:
        """
        Calculate confidence interval for the mean
        Args:
            data: Sample data
            confidence: Confidence level (0 to 1)
        Returns:
            Tuple of (lower bound, upper bound)
        """
        mean = np.mean(data)
        sem = stats.sem(data)
        return stats.t.interval(confidence, len(data)-1, mean, sem)
