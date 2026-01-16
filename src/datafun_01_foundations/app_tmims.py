"""app_tmims.py - Project script.

Author: Tammy Mims
Date: 2026-01

  Practice key Python skills related to:
    - imports
    - logging
    - variables
    - type hints
    - global constants
    - f-strings
    - functions
    - main function
    - conditional execution guard

OBS:
  This is your file to practice and customize.

"""


# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import logging
import statistics
from typing import Final

from datafun_toolkit.logger import get_logger, log_header

# === CONFIGURE LOGGER ONCE PER MODULE (PYTHON FILE) ===

LOG: logging.Logger = get_logger("P01", level="INFO")


# === DECLARE GLOBAL CONSTANTS ===

# All these global variables are CONSTANT, they do NOT change when the program runs.
# By convention, constants are named in UPPERCASE_WITH_UNDERSCORES.
# The following illustrates variables that hold these common types:
#    str, int, float, bool, list of strings.
# `Final` is added to indicate these variables should not be reassigned.
# Examples:

MY_ANALYTICS_COMPANY: Final[str] = "DataFun Analytics"
MY_EMPLOYEE_COUNT: Final[int] = 150

# See the other file for examples.
MY_OCCUPATION: Final[str] = "High School Mathematics Teacher"
MY_YEARS_EXPERIENCE: Final[int] = 31
MY_AVERAGE_UNDERGRAD_GPA: Final[float] = 3.93
IS_CERTIFIED: Final[bool] = True
MY_TEACHING_STRATEGIES: Final[list[str]] = [
    "Problem Solving",
    "Guided Practice",
    "Critical Thinking Exercises",
    "Multiple Representations",
]


# === DECLARE A FUNCTION TO FORMAT THE INFORMATION ===


def get_summary() -> str:
    """Get a formatted summary of the information held in the global variables.

    Arguments: None (nothing is passed in the parentheses after `get_summary`).

    Returns: - a formatted multi-line string (starts with f and wrapped in triple quotes).
    """
    # Create and return a multi-line f-string (triple-quoted) that includes
    # all of the global variables you declared above, each on its own line,
    # labeled clearly with descriptive text.
    summary: str = f"""
    My Professional Information:
        Company: {MY_ANALYTICS_COMPANY}
        Employee Count: {MY_EMPLOYEE_COUNT}
        Occupation: {MY_OCCUPATION}
        Years of Experience: {MY_YEARS_EXPERIENCE}
        Undergraduate GPAC: {MY_AVERAGE_UNDERGRAD_GPA:.2f}
        Is Certified : {IS_CERTIFIED}
        Teaching Strategies: {MY_TEACHING_STRATEGIES}
    """

    LOG.info("Generated formatted multi-line SUMMARY string.")
    LOG.info("Returning the str to the calling function.")
    return summary


# === DECLARE A FUNCTION TO FORMAT DESCRIPTIVE STATISTICS ===


def get_statistics() -> str:
    """Get a formatted summary showing descriptive statistics.

    Arguments: None (nothing is passed in the parentheses).

    Returns: - a formatted multi-line string.
    """
    # Initialize sample data - snowfall measurements in inches.
    snowfall_inches: list[float] = [2.5, 3.5, 2.3, 5.5, 6.5]

    # Calculate descriptive statistics below - see other file for examples.

    total: float = sum(snowfall_inches)
    count: int = len(snowfall_inches)

    minimum: float = min(snowfall_inches) if count > 0 else 0.0
    maximum: float = max(snowfall_inches) if count > 0 else 0.0

    average: float = statistics.mean(snowfall_inches) if count > 0 else 0.0
    stdev: float = statistics.stdev(snowfall_inches) if count > 1 else 0.0

    # Build a formatted multi-line string using f and triple quotes.
    summary: str = f"""
    Descriptive Statistics for Snowfall (inches):
        Total snowfall: {total:.2f} inches
        Count of measurements: {count}
        Minimum snowfall: {minimum:.2f} inches
        Maximum snowfall: {maximum:.2f} inches
        Average snowfall: {average:.2f} inches
        Standard deviation: {stdev:.2f} inches
    """

    LOG.info("Generated formatted multi-line SUMMARY string.")
    LOG.info("Returning the str to the calling function.")
    return summary


# === DEFINE THE MAIN FUNCTION THAT CALLS OTHER FUNCTIONS ===


def main() -> None:
    """Entry point when running this file as a Python script.

    Arguments: None.

    Returns: None.
    """
    # Log a header for the application.
    LOG.info("=================")
    log_header(LOG, "Foundations of Professional Python")
    LOG.info("=================")

    # Log start of main processing.
    LOG.info("START main()..................")

    # Call functions to get formatted strings and log them.
    summary: str = get_summary()
    LOG.info(summary)

    stats: str = get_statistics()
    LOG.info(stats)

    # Log end of main processing.
    LOG.info("END main()..................")


# === CONDITIONAL EXECUTION GUARD ===

# WHY: If running this file as a script, then call main() function.
# OBS: This is just standard Python boilerplate.

if __name__ == "__main__":
    main()
