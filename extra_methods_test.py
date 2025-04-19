from extra_methods import (
    get_user_by_id,
    get_all_projects,
    get_bandits_by_project,
    get_transactions_by_user,
    reset_bandit_stats,
    add_bandit
)

print(" Testing get_user_by_id(3):")
print(get_user_by_id(3))

print("\n Testing get_all_projects():")
for project in get_all_projects():
    print(project)

print("\n Testing get_bandits_by_project(1):")
for bandit in get_bandits_by_project(1):
    print(bandit)

print("\n Testing get_transactions_by_user(3):")
for transaction in get_transactions_by_user(3):
    print(transaction)

print("\n Testing reset_bandit_stats(1):")
reset_bandit_stats(1)

print("\n Testing add_bandit(project_id=1, bandit_name='Layout C'):")
add_bandit(1, 'Layout C')
