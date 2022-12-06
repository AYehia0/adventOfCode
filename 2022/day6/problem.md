# [Advent of Code](/)

-   [\[About\]](/2022/about)
-   [\[Events\]](/2022/events)
-   <a href="https://teespring.com/stores/advent-of-code"
    target="_blank">[Shop]</a>
-   [\[Settings\]](/2022/settings)
-   [\[Log Out\]](/2022/auth/logout)

Yehia <span class="star-count">10\*</span>

#    <span class="title-event-wrap">$year=</span>[2022](/2022)<span class="title-event-wrap">;</span>

-   [\[Calendar\]](/2022)
-   [\[AoC++\]](/2022/support)
-   [\[Sponsors\]](/2022/sponsors)
-   [\[Leaderboard\]](/2022/leaderboard)
-   [\[Stats\]](/2022/stats)

Our [sponsors](/2022/sponsors) help make Advent of Code possible:

<a href="https://www.creetion.nl/publicaties/advent-of-code-2022/"
target="_blank"
onclick="if(ga)ga(&#39;send&#39;,&#39;event&#39;,&#39;sponsor&#39;,&#39;sidebar&#39;,this.href);"
rel="noopener">Creetion</a> - Coding en consultancy combineren in een
leuke job? Kom langs!

## --- Day 6: Tuning Trouble ---

The preparations are finally complete; you and the Elves leave camp on
foot and begin to make your way toward the *star* fruit grove.

As you move through the dense undergrowth, one of the Elves gives you a
handheld *device*. He says that it has many fancy features, but the most
important one to set up right now is the *communication system*.

However, because he's heard you have [significant](/2016/day/6)
[experience](/2016/day/25) [dealing](/2019/day/7) [with](/2019/day/9)
[signal-based](/2019/day/16) [systems](/2021/day/25), he convinced the
other Elves that it would be okay to give you their one malfunctioning
device - surely you'll have no problem fixing it.

As if inspired by comedic timing, the device emits a few <span
title="The magic smoke, on the other hand, seems to be contained... FOR NOW!">colorful
sparks</span>.

To be able to communicate with the Elves, the device needs to *lock on
to their signal*. The signal is a series of seemingly-random characters
that the device receives one at a time.

To fix the communication system, you need to add a subroutine to the
device that detects a *start-of-packet marker* in the datastream. In the
protocol being used by the Elves, the start of a packet is indicated by
a sequence of *four characters that are all different*.

The device will send your subroutine a datastream buffer (your puzzle
input); your subroutine needs to identify the first position where the
four most recently received characters were all different. Specifically,
it needs to report the number of characters from the beginning of the
buffer to the end of the first such four-character marker.

For example, suppose you receive the following datastream buffer:

    mjqjpqmgbljsphdztnvjfqwrcgsmlb

After the first three characters (`mjq`) have been received, there
haven't been enough characters received yet to find the marker. The
first time a marker could occur is after the fourth character is
received, making the most recent four characters `mjqj`. Because `j` is
repeated, this isn't a marker.

The first time a marker appears is after the *seventh* character
arrives. Once it does, the last four characters received are `jpqm`,
which are all different. In this case, your subroutine should report the
value *`7`*, because the first start-of-packet marker is complete after
7 characters have been processed.

Here are a few more examples:

-   `bvwbjplbgvbhsrlpgdmjqwftvncz`: first marker after character *`5`*
-   `nppdvjthqldpwncqszvftbrmjlhg`: first marker after character *`6`*
-   `nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg`: first marker after character
    *`10`*
-   `zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw`: first marker after character
    *`11`*

*How many characters need to be processed before the first
start-of-packet marker is detected?*

To begin, <a href="6/input" target="_blank">get your puzzle input</a>.

Answer:

You can also <span class="share">\[Share<span class="share-content">on
<a
href="https://twitter.com/intent/tweet?text=%22Tuning+Trouble%22+%2D+Day+6+%2D+Advent+of+Code+2022&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2022%2Fday%2F6&amp;related=ericwastl&amp;hashtags=AdventOfCode"
target="_blank">Twitter</a> <a href="javascript:void(0);"
onclick="var mastodon_instance=prompt(&#39;Mastodon Instance / Server Name?&#39;); if(typeof mastodon_instance===&#39;string&#39; &amp;&amp; mastodon_instance.length){this.href=&#39;https://&#39;+mastodon_instance+&#39;/share?text=%22Tuning+Trouble%22+%2D+Day+6+%2D+Advent+of+Code+2022+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2022%2Fday%2F6&#39;}else{return false;}"
target="_blank">Mastodon</a></span>\]</span> this puzzle.
