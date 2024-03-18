from datetime import datetime, timedelta

print(*list(map(
      int, str((datetime.now() + timedelta(days=int(input()))).date()).split('-')))[::-1][:2])
