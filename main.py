import re
import datetime

def write_ids(file_name: str, ids: list[str]):
    with open(file_name, 'x') as w_file:
        for u_id in ids:
            w_file.write(f"{u_id}\n")

if __name__ == "__main__":
    with open("logs_screenshots.txt", encoding='utf-8') as input_f:
        log_file_content = input_f.read()

        # Extract IDs after "Steam error" and "Done" messages, preserving order and making them unique
        error_ids = []
        success_ids = []

        error_set = set()
        success_set = set()

        for match in re.finditer(r"\[(\d+)\] Error", log_file_content):
            error_id = match.group(1)
            if error_id not in error_set:
                error_ids.append(error_id)
                error_set.add(error_id)

        for match in re.finditer(r"\[(\d+)\] Success", log_file_content):
            success_id = match.group(1)
            if success_id not in success_set:
                success_ids.append(success_id)
                success_set.add(success_id)

        time_now  = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S')
        write_ids(f"error_screenshots_ids_{time_now}_.txt", error_ids)
        write_ids(f"success_screenshots_ids_{time_now}_.txt", success_ids)
