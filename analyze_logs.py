def analyze_logs(file_path):
    user_count = {}
    action_count = {}

    with open(file_path, "r") as f:
        for line in f:
            timestamp, user, action = line.strip().split(",")

            user_count[user] = user_count.get(user, 0) + 1
            action_count[action] = action_count.get(action, 0) + 1

    most_active_user = max(user_count, key=user_count.get)
    most_common_action = max(action_count, key=action_count.get)

    return most_active_user, most_common_action


if __name__ == "__main__":
    user, action = analyze_logs("logs.txt")

    print("Most Active User:", user)
    print("Most Common Action:", action)