# Ingest report

Written by `uv run p2 ingest`.
It lists every document in this corpus that ingest added, with what the cleaning pass did and anything that looks wrong.
Running ingest again adds to the table and replaces the "last run" section, and `uv run p2 ingest --report` rewrites it for the documents in docs/ now, after you removed some.

## Summary

- Documents: 240 (the final check needs at least 200)
- Words: 568,523
- Estimated tokens (words times 1.4): 795,932 (`p2 check` warns above 800,000 and fails above 1,000,000)
- Flagged documents: 1

## Documents

| docid | words | characters per page | flags | cleaning |
|---|---:|---:|---|---|
| `nhess-18-1141-2018__p001-004` | 2,626 | 4641 | - | 4 running line(s) removed; reference list dropped, 7,688 characters (heading) |
| `nhess-18-1141-2018__p005-008` | 2,735 | 4344 | - | 4 running line(s) removed; reference list dropped, 7,688 characters (heading) |
| `nhess-18-1141-2018__p009-012` | 1,417 | 2366 | - | 4 running line(s) removed; reference list dropped, 7,688 characters (heading) |
| `nhess-18-1141-2018__p013-016` | 3,028 | 5182 | - | 4 running line(s) removed; reference list dropped, 7,688 characters (heading) |
| `nhess-18-1141-2018__p017-018` | 358 | 1273 | - | 4 running line(s) removed; reference list dropped, 7,688 characters (heading) |
| `nhess-18-1173-2018__p001-004` | 2,708 | 4493 | - | 4 running line(s) removed |
| `nhess-18-1173-2018__p009-012` | 2,043 | 3373 | - | 4 running line(s) removed |
| `nhess-18-1173-2018__p013-014` | 1,677 | 5700 | - | 4 running line(s) removed |
| `nhess-18-2537-2018__p001-004` | 3,550 | 5671 | - | 4 running line(s) removed; reference list dropped, 12,801 characters (heading) |
| `nhess-18-2537-2018__p005-008` | 1,864 | 2916 | - | 4 running line(s) removed; reference list dropped, 12,801 characters (heading) |
| `nhess-18-2537-2018__p009-012` | 2,230 | 3305 | - | 4 running line(s) removed; reference list dropped, 12,801 characters (heading) |
| `nhess-18-2537-2018__p013-016` | 2,286 | 3506 | - | 4 running line(s) removed; reference list dropped, 12,801 characters (heading) |
| `nhess-18-2537-2018__p017-020` | 3,639 | 5765 | - | 4 running line(s) removed; reference list dropped, 12,801 characters (heading) |
| `nhess-18-2697-2018__p001-004` | 2,870 | 4802 | - | 4 running line(s) removed; reference list dropped, 13,359 characters (heading) |
| `nhess-18-2697-2018__p005-008` | 2,378 | 3678 | - | 4 running line(s) removed; reference list dropped, 13,359 characters (heading) |
| `nhess-18-2697-2018__p009-012` | 3,118 | 4624 | - | 4 running line(s) removed; reference list dropped, 13,359 characters (heading) |
| `nhess-18-2697-2018__p013-016` | 2,905 | 4467 | - | 4 running line(s) removed; reference list dropped, 13,359 characters (heading) |
| `nhess-18-2697-2018__p017-020` | 1,098 | 1872 | - | 4 running line(s) removed; reference list dropped, 13,359 characters (heading) |
| `nhess-18-383-2018__p001-004` | 2,817 | 4584 | - | 4 running line(s) removed |
| `nhess-18-383-2018__p005-008` | 2,722 | 4193 | - | 4 running line(s) removed |
| `nhess-18-383-2018__p009-012` | 2,872 | 4100 | - | 4 running line(s) removed |
| `nhess-18-383-2018__p013-014` | 1,214 | 4428 | - | 4 running line(s) removed |
| `nhess-18-571-2018__p001-004` | 2,453 | 4030 | - | 4 running line(s) removed; reference list dropped, 4,961 characters (heading) |
| `nhess-18-571-2018__p005-008` | 1,164 | 1786 | - | 4 running line(s) removed; reference list dropped, 4,961 characters (heading) |
| `nhess-18-571-2018__p009-012` | 1,855 | 2866 | - | 4 running line(s) removed; reference list dropped, 4,961 characters (heading) |
| `nhess-18-759-2018__p001-004` | 2,393 | 3572 | - | 2 running line(s) removed |
| `nhess-18-759-2018__p005-006` | 1,528 | 4872 | - | 2 running line(s) removed |
| `nhess-19-2011-2019__p001-004` | 3,138 | 5142 | - | 4 running line(s) removed |
| `nhess-19-2011-2019__p009-012` | 2,409 | 3528 | - | 4 running line(s) removed |
| `nhess-19-2011-2019__p013-016` | 2,481 | 4170 | - | 4 running line(s) removed |
| `nhess-19-269-2019__p001-004` | 3,433 | 5690 | - | 4 running line(s) removed; reference list dropped, 8,697 characters (heading) |
| `nhess-19-269-2019__p005-008` | 3,491 | 5329 | - | 4 running line(s) removed; reference list dropped, 8,697 characters (heading) |
| `nhess-19-269-2019__p009-012` | 3,603 | 4650 | - | 4 running line(s) removed; reference list dropped, 8,697 characters (heading) |
| `nhess-19-269-2019__p013-017` | 2,399 | 3152 | - | 4 running line(s) removed; reference list dropped, 8,697 characters (heading) |
| `nhess-20-1783-2020__p013-016` | 2,243 | 3571 | - | 4 running line(s) removed; reference list dropped, 11,405 characters (heading) |
| `nhess-20-1941-2020__p001-004` | 3,084 | 4867 | - | 4 running line(s) removed; reference list dropped, 7,531 characters (heading) |
| `nhess-20-1941-2020__p005-008` | 3,106 | 4605 | - | 4 running line(s) removed; reference list dropped, 7,531 characters (heading) |
| `nhess-20-1941-2020__p009-013` | 2,839 | 3480 | - | 4 running line(s) removed; reference list dropped, 7,531 characters (heading) |
| `nhess-20-2873-2020__p001-004` | 2,883 | 4667 | - | 4 running line(s) removed |
| `nhess-20-2873-2020__p005-008` | 2,407 | 3506 | - | 4 running line(s) removed |
| `nhess-20-2873-2020__p009-012` | 2,285 | 3530 | - | 4 running line(s) removed |
| `nhess-20-2873-2020__p013-016` | 3,167 | 5823 | - | 4 running line(s) removed |
| `nhess-20-3551-2020__p001-004` | 2,871 | 4834 | - | 4 running line(s) removed |
| `nhess-20-3551-2020__p005-008` | 2,383 | 3797 | - | 4 running line(s) removed |
| `nhess-20-3551-2020__p009-012` | 1,955 | 2863 | - | 4 running line(s) removed |
| `nhess-20-3551-2020__p013-016` | 2,920 | 4808 | - | 4 running line(s) removed |
| `nhess-20-3551-2020__p017-020` | 400 | 667 | - | 4 running line(s) removed |
| `nhess-20-3551-2020__p021-024` | 571 | 852 | - | 4 running line(s) removed |
| `nhess-20-3551-2020__p025-026` | 1,375 | 5474 | - | 4 running line(s) removed |
| `nhess-21-533-2021__p005-008` | 2,709 | 4121 | - | 4 running line(s) removed; reference list dropped, 14,777 characters (heading) |
| `nhess-21-533-2021__p009-012` | 2,096 | 3093 | - | 4 running line(s) removed; reference list dropped, 14,777 characters (heading) |
| `nhess-21-533-2021__p013-016` | 2,821 | 4381 | - | 4 running line(s) removed; reference list dropped, 14,777 characters (heading) |
| `nhess-21-533-2021__p017-020` | 1,405 | 2160 | - | 4 running line(s) removed; reference list dropped, 14,777 characters (heading) |
| `nhess-21-533-2021__p021-025` | 403 | 487 | - | 4 running line(s) removed; reference list dropped, 14,777 characters (heading) |
| `nhess-21-757-2021__p001-004` | 3,028 | 4862 | - | 4 running line(s) removed; reference list dropped, 11,790 characters (heading) |
| `nhess-21-757-2021__p005-008` | 2,597 | 3842 | - | 4 running line(s) removed; reference list dropped, 11,790 characters (heading) |
| `nhess-21-757-2021__p009-012` | 2,359 | 3467 | - | 4 running line(s) removed; reference list dropped, 11,790 characters (heading) |
| `nhess-21-757-2021__p013-016` | 3,127 | 4943 | - | 4 running line(s) removed; reference list dropped, 11,790 characters (heading) |
| `nhess-22-3501-2022__p001-004` | 3,356 | 5473 | - | 4 running line(s) removed |
| `nhess-22-3501-2022__p005-008` | 2,672 | 4222 | - | 4 running line(s) removed |
| `nhess-22-3501-2022__p009-012` | 1,446 | 2298 | - | 4 running line(s) removed |
| `nhess-22-3501-2022__p013-016` | 2,132 | 3508 | - | 4 running line(s) removed |
| `nhess-22-3501-2022__p017-020` | 1,661 | 2762 | - | 4 running line(s) removed |
| `nhess-22-3501-2022__p021-025` | 2,960 | 4268 | - | 4 running line(s) removed |
| `nhess-23-1719-2023__p001-004` | 2,953 | 4920 | - | 4 running line(s) removed; reference list dropped, 19,326 characters (heading) |
| `nhess-23-1719-2023__p005-008` | 2,334 | 3867 | - | 4 running line(s) removed; reference list dropped, 19,326 characters (heading) |
| `nhess-23-1719-2023__p009-012` | 2,300 | 3624 | - | 4 running line(s) removed; reference list dropped, 19,326 characters (heading) |
| `nhess-23-1719-2023__p013-016` | 2,547 | 4143 | - | 4 running line(s) removed; reference list dropped, 19,326 characters (heading) |
| `nhess-23-1719-2023__p017-020` | 3,225 | 5334 | - | 4 running line(s) removed; reference list dropped, 19,326 characters (heading) |
| `nhess-23-1719-2023__p021-024` | 394 | 698 | - | 4 running line(s) removed; reference list dropped, 19,326 characters (heading) |
| `nhess-23-2089-2023__p001-004` | 2,901 | 4773 | - | 4 running line(s) removed; reference list dropped, 21,838 characters (heading) |
| `nhess-23-2089-2023__p005-008` | 2,719 | 4347 | - | 4 running line(s) removed; reference list dropped, 21,838 characters (heading) |
| `nhess-23-2089-2023__p009-012` | 2,321 | 3558 | - | 4 running line(s) removed; reference list dropped, 21,838 characters (heading) |
| `nhess-23-2089-2023__p013-016` | 2,314 | 3669 | - | 4 running line(s) removed; reference list dropped, 21,838 characters (heading) |
| `nhess-23-2089-2023__p017-020` | 1,480 | 2484 | - | 4 running line(s) removed; reference list dropped, 21,838 characters (heading) |
| `nhess-23-2523-2023__p001-004` | 2,269 | 3588 | - | 4 running line(s) removed; reference list dropped, 3,919 characters (heading) |
| `nhess-23-2523-2023__p005-008` | 1,129 | 1760 | - | 4 running line(s) removed; reference list dropped, 3,919 characters (heading) |
| `nhess-23-2895-2023__p001-004` | 3,145 | 5069 | - | 4 running line(s) removed; reference list dropped, 11,307 characters (heading) |
| `nhess-23-2895-2023__p005-008` | 1,601 | 2442 | - | 4 running line(s) removed; reference list dropped, 11,307 characters (heading) |
| `nhess-23-2895-2023__p009-012` | 1,648 | 2482 | - | 4 running line(s) removed; reference list dropped, 11,307 characters (heading) |
| `nhess-23-2895-2023__p013-016` | 2,889 | 4586 | - | 4 running line(s) removed; reference list dropped, 11,307 characters (heading) |
| `nhess-23-2895-2023__p017-020` | 1,151 | 1913 | - | 4 running line(s) removed; reference list dropped, 11,307 characters (heading) |
| `nhess-23-293-2023__p001-004` | 3,064 | 4859 | - | 4 running line(s) removed |
| `nhess-23-293-2023__p005-008` | 3,003 | 4261 | - | 4 running line(s) removed |
| `nhess-23-293-2023__p009-012` | 2,486 | 3884 | - | 4 running line(s) removed |
| `nhess-23-293-2023__p013-016` | 3,406 | 5374 | - | 4 running line(s) removed |
| `nhess-23-293-2023__p017-020` | 1,406 | 1959 | - | 4 running line(s) removed |
| `nhess-23-293-2023__p021-023` | 1,907 | 4872 | - | 4 running line(s) removed |
| `nhess-23-3445-2023__p001-004` | 2,614 | 4322 | - | 4 running line(s) removed; reference list dropped, 14,694 characters (heading) |
| `nhess-23-3445-2023__p005-008` | 3,367 | 5183 | - | 4 running line(s) removed; reference list dropped, 14,694 characters (heading) |
| `nhess-23-3445-2023__p009-012` | 2,383 | 3522 | - | 4 running line(s) removed; reference list dropped, 14,694 characters (heading) |
| `nhess-23-3445-2023__p013-016` | 2,882 | 4686 | - | 4 running line(s) removed; reference list dropped, 14,694 characters (heading) |
| `nhess-23-3445-2023__p017-021` | 1,233 | 1669 | - | 4 running line(s) removed; reference list dropped, 14,694 characters (heading) |
| `nhess-24-1779-2024__p001-004` | 3,249 | 5179 | - | 4 running line(s) removed; reference list dropped, 9,532 characters (heading) |
| `nhess-24-1779-2024__p005-008` | 1,812 | 2752 | - | 4 running line(s) removed; reference list dropped, 9,532 characters (heading) |
| `nhess-24-1779-2024__p009-012` | 2,935 | 4324 | - | 4 running line(s) removed; reference list dropped, 9,532 characters (heading) |
| `nhess-24-1779-2024__p013-015` | 679 | 1507 | - | 4 running line(s) removed; reference list dropped, 9,532 characters (heading) |
| `nhess-24-2757-2024__p001-004` | 3,007 | 4724 | - | 4 running line(s) removed |
| `nhess-24-2757-2024__p005-008` | 2,367 | 3485 | - | 4 running line(s) removed |
| `nhess-24-2757-2024__p009-012` | 3,101 | 4911 | - | 4 running line(s) removed |
| `nhess-24-3387-2024__p001-004` | 2,270 | 3654 | - | 4 running line(s) removed; reference list dropped, 9,967 characters (heading) |
| `nhess-24-3387-2024__p005-008` | 2,256 | 3462 | - | 4 running line(s) removed; reference list dropped, 9,967 characters (heading) |
| `nhess-24-3387-2024__p009-012` | 2,444 | 4010 | - | 4 running line(s) removed; reference list dropped, 9,967 characters (heading) |
| `nhess-24-3387-2024__p013-014` | 132 | 456 | - | 4 running line(s) removed; reference list dropped, 9,967 characters (heading) |
| `nhess-25-1255-2025__p001-004` | 3,163 | 5240 | - | 4 running line(s) removed; reference list dropped, 10,884 characters (heading) |
| `nhess-25-1255-2025__p005-008` | 2,753 | 4398 | - | 4 running line(s) removed; reference list dropped, 10,884 characters (heading) |
| `nhess-25-1255-2025__p009-012` | 3,269 | 5095 | - | 4 running line(s) removed; reference list dropped, 10,884 characters (heading) |
| `nhess-25-1255-2025__p013-016` | 2,321 | 3564 | - | 4 running line(s) removed; reference list dropped, 10,884 characters (heading) |
| `nhess-25-1255-2025__p017-020` | 3,651 | 5922 | - | 4 running line(s) removed; reference list dropped, 10,884 characters (heading) |
| `nhess-25-1255-2025__p029-032` | 641 | 1036 | - | 4 running line(s) removed; reference list dropped, 10,884 characters (heading) |
| `nhess-25-1255-2025__p033-036` | 354 | 586 | - | 4 running line(s) removed; reference list dropped, 10,884 characters (heading) |
| `nhess-25-1331-2025__p001-004` | 2,436 | 4100 | - | 4 running line(s) removed |
| `nhess-25-1331-2025__p005-008` | 2,708 | 4154 | - | 4 running line(s) removed |
| `nhess-25-1331-2025__p009-012` | 2,048 | 3118 | - | 4 running line(s) removed |
| `nhess-25-1331-2025__p013-016` | 2,591 | 4335 | - | 4 running line(s) removed |
| `nhess-25-1331-2025__p017-021` | 2,481 | 3656 | - | 4 running line(s) removed |
| `nhess-25-1975-2025__p001-004` | 2,703 | 4266 | - | 4 running line(s) removed |
| `nhess-25-1975-2025__p005-008` | 3,002 | 4646 | - | 4 running line(s) removed |
| `nhess-25-1975-2025__p009-012` | 3,089 | 4891 | - | 4 running line(s) removed |
| `nhess-25-1975-2025__p013-017` | 3,299 | 4730 | - | 4 running line(s) removed |
| `nhess-25-2215-2025__p001-004` | 2,996 | 4919 | - | 4 running line(s) removed |
| `nhess-25-2215-2025__p005-009` | 3,197 | 4617 | - | 4 running line(s) removed |
| `nhess-25-3333-2025__p001-004` | 2,900 | 4949 | - | 4 running line(s) removed; reference list dropped, 17,181 characters (heading) |
| `nhess-25-3333-2025__p005-008` | 2,237 | 3684 | - | 4 running line(s) removed; reference list dropped, 17,181 characters (heading) |
| `nhess-25-3333-2025__p009-012` | 2,212 | 3772 | - | 4 running line(s) removed; reference list dropped, 17,181 characters (heading) |
| `nhess-25-3333-2025__p013-016` | 2,195 | 3793 | - | 4 running line(s) removed; reference list dropped, 17,181 characters (heading) |
| `nhess-25-3333-2025__p017-021` | 356 | 498 | - | 4 running line(s) removed; reference list dropped, 17,181 characters (heading) |
| `nhess-25-4503-2025__p001-004` | 3,071 | 5234 | - | 4 running line(s) removed; reference list dropped, 14,567 characters (heading) |
| `nhess-25-4503-2025__p005-008` | 3,024 | 4879 | - | 4 running line(s) removed; reference list dropped, 14,567 characters (heading) |
| `nhess-25-4503-2025__p009-012` | 1,975 | 3127 | - | 4 running line(s) removed; reference list dropped, 14,567 characters (heading) |
| `nhess-25-4503-2025__p013-016` | 2,567 | 4309 | - | 4 running line(s) removed; reference list dropped, 14,567 characters (heading) |
| `nhess-25-4503-2025__p017-020` | 974 | 1573 | - | 4 running line(s) removed; reference list dropped, 14,567 characters (heading) |
| `nhess-25-4503-2025__p021-023` | 299 | 698 | - | 4 running line(s) removed; reference list dropped, 14,567 characters (heading) |
| `nhess-25-5033-2025__p001-004` | 2,102 | 3349 | - | 4 running line(s) removed |
| `nhess-25-5033-2025__p005-008` | 2,674 | 4131 | - | 4 running line(s) removed |
| `nhess-25-5033-2025__p009-012` | 2,771 | 4154 | - | 4 running line(s) removed |
| `nhess-25-5033-2025__p013-016` | 1,909 | 2992 | - | 4 running line(s) removed |
| `nhess-25-5033-2025__p017-021` | 3,344 | 4926 | - | 4 running line(s) removed |
| `nhess-25-625-2025__p001-004` | 2,657 | 4501 | - | 4 running line(s) removed; reference list dropped, 16,817 characters (heading) |
| `nhess-25-625-2025__p005-008` | 2,449 | 3942 | - | 4 running line(s) removed; reference list dropped, 16,817 characters (heading) |
| `nhess-25-625-2025__p009-012` | 1,781 | 2954 | - | 4 running line(s) removed; reference list dropped, 16,817 characters (heading) |
| `nhess-25-625-2025__p013-016` | 2,611 | 4406 | - | 4 running line(s) removed; reference list dropped, 16,817 characters (heading) |
| `nhess-25-625-2025__p017-020` | 1,635 | 2747 | - | 4 running line(s) removed; reference list dropped, 16,817 characters (heading) |
| `nhess-26-1059-2026__p005-008` | 2,756 | 4499 | - | 4 running line(s) removed; reference list dropped, 11,385 characters (heading) |
| `nhess-26-1059-2026__p009-012` | 1,720 | 2850 | - | 4 running line(s) removed; reference list dropped, 11,385 characters (heading) |
| `nhess-26-1059-2026__p013-016` | 1,590 | 2720 | - | 4 running line(s) removed; reference list dropped, 11,385 characters (heading) |
| `nhess-26-1161-2026__p001-004` | 2,836 | 4846 | - | 4 running line(s) removed; reference list dropped, 8,726 characters (heading) |
| `nhess-26-1161-2026__p005-008` | 2,796 | 4536 | - | 4 running line(s) removed; reference list dropped, 8,726 characters (heading) |
| `nhess-26-1161-2026__p009-012` | 1,732 | 2754 | - | 4 running line(s) removed; reference list dropped, 8,726 characters (heading) |
| `nhess-26-1161-2026__p013-016` | 2,603 | 4557 | - | 4 running line(s) removed; reference list dropped, 8,726 characters (heading) |
| `nhess-26-1161-2026__p017-021` | 1,321 | 1800 | - | 4 running line(s) removed; reference list dropped, 8,726 characters (heading) |
| `nhess-26-4353-2026` | 1,026 | 2456 | - | reference list dropped, 532 characters (heading) |
| `tc-12-1121-2018__p001-004` | 2,518 | 4022 | - | 4 running line(s) removed; reference list dropped, 10,858 characters (heading) |
| `tc-12-1121-2018__p005-008` | 2,402 | 3573 | - | 4 running line(s) removed; reference list dropped, 10,858 characters (heading) |
| `tc-12-1121-2018__p009-012` | 1,955 | 2934 | - | 4 running line(s) removed; reference list dropped, 10,858 characters (heading) |
| `tc-12-1121-2018__p013-015` | 1,105 | 2389 | - | 4 running line(s) removed; reference list dropped, 10,858 characters (heading) |
| `tc-12-3759-2018__p001-004` | 3,552 | 5528 | - | 4 running line(s) removed |
| `tc-12-3759-2018__p005-008` | 2,139 | 3156 | - | 4 running line(s) removed |
| `tc-12-3759-2018__p009-012` | 2,819 | 4130 | - | 4 running line(s) removed |
| `tc-12-3759-2018__p013-016` | 3,175 | 5335 | - | 4 running line(s) removed |
| `tc-13-3225-2019__p013-014` | 1,309 | 4947 | - | 4 running line(s) removed |
| `tc-13-3353-2019__p001-004` | 3,057 | 4850 | - | 4 running line(s) removed |
| `tc-13-3353-2019__p009-012` | 2,467 | 4006 | - | 4 running line(s) removed |
| `tc-13-3353-2019__p013-014` | 1,275 | 5126 | - | 4 running line(s) removed |
| `tc-14-115-2020__p001-004` | 2,539 | 4073 | - | 4 running line(s) removed |
| `tc-14-115-2020__p009-012` | 3,297 | 5082 | - | 4 running line(s) removed |
| `tc-14-115-2020__p013-016` | 2,809 | 5021 | - | 4 running line(s) removed |
| `tc-14-131-2020__p001-004` | 2,935 | 4790 | - | 4 running line(s) removed |
| `tc-14-131-2020__p005-008` | 2,791 | 4334 | - | 4 running line(s) removed |
| `tc-14-131-2020__p009-012` | 3,236 | 5100 | - | 4 running line(s) removed |
| `tc-14-131-2020__p013-015` | 2,219 | 5600 | - | 4 running line(s) removed |
| `tc-14-3381-2020__p001-004` | 3,062 | 4834 | - | 4 running line(s) removed |
| `tc-14-3381-2020__p005-008` | 2,366 | 3386 | - | 4 running line(s) removed |
| `tc-14-3381-2020__p009-012` | 2,638 | 3912 | - | 4 running line(s) removed |
| `tc-14-3381-2020__p013-016` | 1,615 | 2507 | - | 4 running line(s) removed |
| `tc-14-3381-2020__p017-018` | 1,647 | 5893 | - | 4 running line(s) removed |
| `tc-14-737-2020__p001-004` | 3,344 | 5216 | - | 4 running line(s) removed; reference list dropped, 11,685 characters (heading) |
| `tc-14-737-2020__p005-008` | 2,877 | 4292 | - | 4 running line(s) removed; reference list dropped, 11,685 characters (heading) |
| `tc-14-737-2020__p009-012` | 3,595 | 5699 | - | 4 running line(s) removed; reference list dropped, 11,685 characters (heading) |
| `tc-15-1567-2021__p001-004` | 2,928 | 5110 | - | 4 running line(s) removed |
| `tc-15-1567-2021__p005-008` | 2,368 | 3834 | - | 4 running line(s) removed |
| `tc-15-1567-2021__p009-012` | 2,255 | 3648 | - | 4 running line(s) removed |
| `tc-15-1567-2021__p013-016` | 2,476 | 4155 | - | 4 running line(s) removed |
| `tc-15-1567-2021__p017-020` | 2,357 | 4384 | - | 4 running line(s) removed |
| `tc-15-3293-2021__p001-004` | 3,183 | 5108 | - | 4 running line(s) removed; reference list dropped, 8,798 characters (heading) |
| `tc-15-3293-2021__p005-008` | 2,927 | 4302 | - | 4 running line(s) removed; reference list dropped, 8,798 characters (heading) |
| `tc-15-3293-2021__p009-012` | 2,351 | 3585 | - | 4 running line(s) removed; reference list dropped, 8,798 characters (heading) |
| `tc-15-3293-2021__p013-016` | 2,199 | 3466 | - | 4 running line(s) removed; reference list dropped, 8,798 characters (heading) |
| `tc-15-3293-2021__p017-020` | 1,376 | 2113 | - | 4 running line(s) removed; reference list dropped, 8,798 characters (heading) |
| `tc-15-3293-2021__p021-023` | 273 | 608 | - | 4 running line(s) removed; reference list dropped, 8,798 characters (heading) |
| `tc-15-3539-2021__p001-004` | 2,901 | 4640 | - | 4 running line(s) removed |
| `tc-15-3539-2021__p005-008` | 2,832 | 4196 | - | 4 running line(s) removed |
| `tc-15-3539-2021__p009-012` | 2,927 | 4385 | - | 4 running line(s) removed |
| `tc-15-3539-2021__p013-015` | 2,429 | 5794 | - | 4 running line(s) removed |
| `tc-15-3813-2021__p005-008` | 2,387 | 3912 | - | 4 running line(s) removed |
| `tc-15-3813-2021__p009-012` | 1,872 | 3035 | - | 4 running line(s) removed |
| `tc-15-3813-2021__p013-016` | 2,913 | 5109 | - | 4 running line(s) removed |
| `tc-15-3813-2021__p017-020` | 231 | 395 | scanned-looking (395 characters per page, under 400) | 4 running line(s) removed |
| `tc-15-3813-2021__p021-025` | 2,340 | 3490 | - | 4 running line(s) removed |
| `tc-15-983-2021__p001-004` | 2,429 | 3974 | - | 4 running line(s) removed |
| `tc-15-983-2021__p009-012` | 2,783 | 4235 | - | 4 running line(s) removed |
| `tc-15-983-2021__p017-020` | 1,749 | 2918 | - | 4 running line(s) removed |
| `tc-15-983-2021__p021-022` | 1,055 | 4301 | - | 4 running line(s) removed |
| `tc-16-3393-2022__p001-004` | 2,631 | 4489 | - | 4 running line(s) removed |
| `tc-16-3393-2022__p005-008` | 2,467 | 3943 | - | 4 running line(s) removed |
| `tc-16-3393-2022__p009-012` | 1,610 | 2574 | - | 4 running line(s) removed |
| `tc-16-3393-2022__p013-016` | 1,760 | 3121 | - | 4 running line(s) removed |
| `tc-16-3393-2022__p017-019` | 1,699 | 4440 | - | 4 running line(s) removed |
| `tc-17-1475-2023__p001-004` | 2,607 | 4188 | - | 4 running line(s) removed; reference list dropped, 15,036 characters (heading) |
| `tc-17-1475-2023__p005-008` | 2,868 | 4448 | - | 4 running line(s) removed; reference list dropped, 15,036 characters (heading) |
| `tc-17-1475-2023__p009-012` | 2,305 | 3608 | - | 4 running line(s) removed; reference list dropped, 15,036 characters (heading) |
| `tc-17-1475-2023__p013-016` | 2,538 | 3965 | - | 4 running line(s) removed; reference list dropped, 15,036 characters (heading) |
| `tc-17-1475-2023__p017-020` | 1,932 | 2934 | - | 4 running line(s) removed; reference list dropped, 15,036 characters (heading) |
| `tc-17-1755-2023__p001-004` | 3,435 | 5522 | - | 4 running line(s) removed |
| `tc-17-1755-2023__p005-008` | 1,910 | 2731 | - | 4 running line(s) removed |
| `tc-17-1755-2023__p009-012` | 2,206 | 3292 | - | 4 running line(s) removed |
| `tc-17-1755-2023__p013-016` | 2,524 | 4026 | - | 4 running line(s) removed |
| `tc-17-1755-2023__p017-019` | 2,270 | 5510 | - | 4 running line(s) removed |
| `tc-17-2245-2023__p001-004` | 3,094 | 5100 | - | 4 running line(s) removed |
| `tc-17-2245-2023__p005-008` | 2,620 | 4057 | - | 4 running line(s) removed |
| `tc-17-2245-2023__p009-012` | 3,421 | 5507 | - | 4 running line(s) removed |
| `tc-17-2245-2023__p013-016` | 3,000 | 5821 | - | 4 running line(s) removed |
| `tc-18-3807-2024__p001-004` | 2,733 | 4483 | - | 4 running line(s) removed; reference list dropped, 12,980 characters (heading) |
| `tc-18-5495-2024__p001-004` | 2,719 | 4527 | - | 4 running line(s) removed |
| `tc-18-5495-2024__p005-008` | 2,549 | 4091 | - | 4 running line(s) removed |
| `tc-18-5495-2024__p009-012` | 2,865 | 4736 | - | 4 running line(s) removed |
| `tc-18-5495-2024__p013-016` | 1,331 | 2256 | - | 4 running line(s) removed |
| `tc-18-5495-2024__p017-020` | 1,298 | 2314 | - | 4 running line(s) removed |
| `tc-18-5495-2024__p021-023` | 2,329 | 6002 | - | 4 running line(s) removed |
| `tc-19-1849-2025__p001-004` | 3,578 | 5784 | - | 4 running line(s) removed; reference list dropped, 29,346 characters (heading) |
| `tc-19-1849-2025__p005-008` | 3,234 | 4801 | - | 4 running line(s) removed; reference list dropped, 29,346 characters (heading) |
| `tc-19-1849-2025__p009-012` | 2,284 | 3488 | - | 4 running line(s) removed; reference list dropped, 29,346 characters (heading) |
| `tc-19-1849-2025__p013-016` | 3,146 | 4827 | - | 4 running line(s) removed; reference list dropped, 29,346 characters (heading) |
| `tc-19-1849-2025__p017-020` | 1,156 | 1919 | - | 4 running line(s) removed; reference list dropped, 29,346 characters (heading) |
| `tc-20-4515-2026__p001-004` | 2,875 | 4702 | - | 4 running line(s) removed |
| `tc-20-4515-2026__p005-008` | 2,567 | 3963 | - | 4 running line(s) removed |
| `tc-20-4515-2026__p009-012` | 998 | 1582 | - | 4 running line(s) removed |
| `tc-20-4515-2026__p013-016` | 3,490 | 5690 | - | 4 running line(s) removed |
| `tc-20-4515-2026__p017-020` | 2,542 | 4330 | - | 4 running line(s) removed |
| `tc-20-4515-2026__p021-022` | 1,363 | 5234 | - | 4 running line(s) removed |

## Not added in the last run

Nothing was left out.

## What to check by eye

Ingest cleans text by rules, and rules miss things.
Take five minutes to open the shortest, a middle one and the longest document next to its original and read one page of each.

- Search the documents for `þ`, `¼`, `(cid:` and the replacement character.
  A hit usually means the PDF's font map is wrong, which no tool can repair, so treat it as a defect and leave that document out.
- Look at the end of a few papers.
  Ingest drops a trailing reference list when it finds a References heading or a run of numbered entries.
  A paper whose list has neither can keep it, and then every author and journal name matches queries it should not.
- Open the first lines of a few documents.
  Author lists, copyright pages and tables of contents are not removed automatically, and you may want to cut them.
- Compare one table with the PDF.
  A PDF prints footnote marks as small raised digits, and the converter glues them onto the word or number next to them: `ALUMINUM1` is the heading ALUMINUM with footnote 1, and `11210,000` can be 210,000 with footnote 11.
  Quotes still match the stored text, but a number read from it can be wrong, so check before you trust a figure in a query, a judgment or an answer.
- Fix the `license` column in the manifest for every document, then run `uv run p2 license`.
  It is `unknown` until you do, and `unknown` does not pass.

## If a document is flagged as scanned

A scan is a picture of a page, so there is no text for ingest to read.
This template does not install an OCR tool, because it is large and most students never need it.
If you do need one, the opt-in route is pymupdf4llm with rapidocr, run on its own outside the template's environment:

```
uv run --no-project --with pymupdf4llm --with rapidocr python -c "import pymupdf4llm, sys, pathlib; pathlib.Path(sys.argv[2]).write_text(pymupdf4llm.to_markdown(sys.argv[1], use_ocr=True, force_ocr=True), encoding='utf-8')" scan.pdf scan.md
```

Put the resulting `.md` file in your folder and ingest the folder again.
It costs about 2 seconds a page, and OCR text needs a second look: it misreads ligatures, hyphens and numbers.
pymupdf4llm is AGPL-3.0 software, so use it only as a tool on your own machine, and do not add it to this repo's dependencies or copy its code into the repo.
