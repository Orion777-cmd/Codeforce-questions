
messages = int(input())
recipients = []
for _ in range(messages):
    recipients.append(input())
unique = set()
ans = []

for i in range(messages-1, -1, -1):
    if recipients[i] not in unique:
        unique.add(recipients[i])
        ans.append(recipients[i])

print(*ans, sep='\n')