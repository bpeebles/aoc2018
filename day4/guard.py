#!/usr/bin/env python3

import re
import attr
import datetime
from collections import defaultdict, Counter


@attr.s
class Day:
    sleeps = attr.ib(default=attr.Factory(list))

@attr.s
class Guard:
    guard_id = attr.ib()
    days = attr.ib()

    def minutes(self):
        for when, day in self.days.items():
            for sleep in day:
                #print(sleep)
                for m in range(sleep[0], sleep[1]):
                    #print(m)
                    yield m

    def total_asleep(self):
        return sum(1 for _ in self.minutes())

    def most_common(self):
        cnt = Counter(self.minutes())
        print(cnt)
        return cnt.most_common(1)[0]


guards = {}
lines = open("input.txt", "r").readlines()
lines.sort()

#lines = open("sample_input.txt", "r").readlines()

guard_id = None
for line in lines:
    dt = re.search(r'(\d\d)-(\d\d)-(\d\d) (\d\d):(\d\d)]', line)
    when = datetime.datetime(year=int(dt.group(1)), month=int(dt.group(2)), day=int(dt.group(3)),
                             hour=int(dt.group(4)), minute=int(dt.group(5)))
    if 'begins' in line:
        guard = re.search(r'#(\d*) ', line)
        guard_id = int(guard.group(1))
    elif 'falls asleep' in line:
        begin_sleep = when
    elif 'wakes up' in line:
        print(guard_id, when, begin_sleep.minute, when.minute)
        if guard_id not in guards:
            guards[guard_id] = Guard(guard_id=guard_id, days=defaultdict(list))
        guards[guard_id].days[when.date()].append((begin_sleep.minute, when.minute))

print(guards)
most = -1
most_guard = None
for guard_id, guard in guards.items():
    asleep = guard.total_asleep()
    print(guard_id)
    print(guard_id, asleep)
    if guard.total_asleep() > most:
        most = asleep
        most_guard = guard

common = most_guard.most_common()
print(most, common)
print(most_guard.guard_id * common[0])

# part 2
most_times = -1
most_minute = None
most_minute_guard = None
for guard_id, guard in guards.items():
    minute, times = guard.most_common()
    if times > most_times:
        most_times = times
        most_minute = minute
        most_minute_guard = guard

print(most_times, most_minute, most_minute_guard)
print(most_minute_guard.guard_id * most_minute)
