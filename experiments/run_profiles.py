import os

from copy_profiles import copy_all_figures
from profiles import Profiles, set_loglevel

COPY_PAPER_FIGURES = False


if __name__ == "__main__":
    cwd = os.getcwd()
    set_loglevel("INFO")

    # Generate the performance and data profiles on the plain problems with n <= 50.
    profiles = Profiles(1, 50, "unconstrained")
    profiles(["CG", "BFGS", "NEWUOA"], ["CG", "BFGS", "PDFO"])
    del profiles

    # Generate the performance and data profiles on the noisy problems with n <= 50 and different noise levels.
    for noise_level in [1e-10, 1e-8]:
        profiles = Profiles(1, 50, "unconstrained", feature="noisy", noise_level=noise_level)
        profiles(["CG", "BFGS", "NEWUOA"], ["CG", "BFGS", "PDFO"])
        del profiles

    # Generate the performance and data profiles on the problems containing NaNs.
    profiles = Profiles(1, 50, "unconstrained", feature="nan", nan_rate=0.01)
    profiles(["CG", "BFGS", "PDFO", "PDFO-(no-barrier)"])
    del profiles

    profiles = Profiles(1, 50, "unconstrained", feature="nan", nan_rate=0.05)
    profiles(["CG", "BFGS", "PDFO", "PDFO-(no-barrier)"])
    del profiles

    # Generate the profiles for the paper.
    os.chdir(cwd)
    if COPY_PAPER_FIGURES:
        copy_all_figures()
