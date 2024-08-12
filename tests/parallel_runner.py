import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import glob

BROWSER = "chrome"

MAX_CONCURRENT_BROWSERS = 2


def run_behave(feature, browser):
    os.system(f"behave {feature} --define browser={browser}")


def run_feature(feature, browser):
    try:
        run_behave(feature, browser)
    except Exception as e:
        print(f"Error running {feature}: {e}")


if __name__ == "__main__":
    features = glob.glob("features/**/*.feature", recursive=True)

    with ThreadPoolExecutor(max_workers=MAX_CONCURRENT_BROWSERS) as executor:
        futures = [executor.submit(run_feature, feature, BROWSER) for feature in features]
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error: {e}")
