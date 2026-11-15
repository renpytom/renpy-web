# Release data for Ren'Py 7.0 to 7.4, newest first.

from model import *

Release(
    prerelease=False,
    invisible=False,
    version="7.4.11",
    pygame="-2.1.0",
    date="December 2, 2021",
    patch=None,
    name="Lucky Beckoning Cat",
    world_order=11,
    announcement="""\
I'd like to announce Ren'Py 7.4.11, the eleventh patch release to Ren'Py
7.4. This is another fix-only release, with a special focus on Android and
ChromeOS support via android.

Check the changelog to see the full list of changes, as there are changes that
affect every platform.

Ren'Py 7.4 is brought to you by:

.. raw:: html

    <table style="width: 100%;">
    <tr>
    <td style="width: 25%; vertical-align: top">
    <ul>
        <li> Andrej
        <li> Andrí Wilford
        <li> Andy_kl
        <li> Capntrips
        <li> Charles Surett
        <li> Cherie Davidson
        <li> CobaltCore
        <li> CodePsy
        <li> Daniel Conley
        <li> Daniel Luque
        <li> Dogtopus
        <li> Eric Ahn
        <li> GanstaKingofSA
        <li> GimmiRuski
        <li> GiovanH
        <li> Gouvernathor
    </ul></td><td style="width: 25%; vertical-align: top"><ul>
        <li> Gratusfr
        <li> Hanaka
        <li> Hyper Sonic
        <li> Jackmcbarn
        <li> Joaquin Garmendia Cabrera
        <li> Joshua Fehler
        <li> Joshua Stone
        <li> Jürg Billeter
        <li> Kapil Gain
        <li> KG
        <li> Kyouryuukunn
        <li> Lee Yunseok
        <li> Lent1
        <li> Lezalith
        <li> Liu Wenyuan
        <li> Loliconazter
    </ul></td><td style="width: 25%; vertical-align: top"><ul>
        <li> Lucas Ramage
        <li> Maciej Katafiasz
        <li> Mal Graty
        <li> Mason Chou
        <li> Maxwell Paul Brickner
        <li> Midgethetree
        <li> Moshibit
        <li> Neotus
        <li> Neyunse
        <li> Paul J Martinez
        <li> Remix
        <li> Ruben Jesus Garcia-Hernandez
        <li> Siege-Wizard
        <li> Shawna-p
    </ul></td><td style="width: 25%; vertical-align: top"><ul>
        <li> Sylvain Beucler
        <li> Uyjulian
        <li> Xavimat
        <li> Zedraxlo
        <li> 被诅咒的章鱼
        <li> 逆转咸鱼
    </ul><td></tr></table>

everyone who's tested this release, and myself, Tom "PyTom" Rothamel.
""",
    history="""\
""",

    full_html="""\
""",

    top_html="""\
""",
)


Release(
    prerelease=False,
    invisible=False,
    version="7.4.10",
    pygame="-2.1.0",
    date="October 23, 2021",
    patch=None,
    name="Lucky Four-Footed Rabbit",
    world_order=11,
    announcement="""\
I'd like to announce Ren'Py 7.4.10, the tenth patch release of Ren'Py
7.4. This release is a small one, to fix a regression in
`Ren'Py 7.4.9 <https://www.renpy.org/release/7.4.9>`_ that
occurred when large images were displayed.

There are also several fixes to the way voice interacts with text
with pauses; the performance of drag and drop; and how the android
port automatically selects an app store.

The Indonesian and Polish language translation has been updated.

Ren'Py 7.4 is brought to you by:

.. raw:: html

    <table style="width: 100%;">
    <tr>
    <td style="width: 25%; vertical-align: top">
    <ul>
        <li> Andrej
        <li> Andrí Wilford
        <li> Andy_kl
        <li> Capntrips
        <li> Charles Surett
        <li> Cherie Davidson
        <li> CobaltCore
        <li> CodePsy
        <li> Daniel Conley
        <li> Daniel Luque
        <li> Dogtopus
        <li> Eric Ahn
        <li> GanstaKingofSA
        <li> GimmiRuski
        <li> GiovanH
        <li> Gouvernathor
    </ul></td><td style="width: 25%; vertical-align: top"><ul>
        <li> Gratusfr
        <li> Hanaka
        <li> Hyper Sonic
        <li> Jackmcbarn
        <li> Jan Masek
        <li> Joaquin Garmendia Cabrera
        <li> Joshua Fehler
        <li> Joshua Stone
        <li> Jürg Billeter
        <li> Kapil Gain
        <li> KG
        <li> Kyouryuukunn
        <li> Lee Yunseok
        <li> Lent1
        <li> Lezalith
        <li> Liu Wenyuan
    </ul></td><td style="width: 25%; vertical-align: top"><ul>
        <li> Loliconazter
        <li> Lucas Ramage
        <li> Maciej Katafiasz
        <li> Mal Graty
        <li> Mason Chou
        <li> Maxwell Paul Brickner
        <li> Midgethetree
        <li> Moshibit
        <li> Neotus
        <li> Neyunse
        <li> Paul J Martinez
        <li> Remix
        <li> Ruben Jesus Garcia-Hernandez
        <li> Siege-Wizard
        <li> Shawna-p
    </ul></td><td style="width: 25%; vertical-align: top"><ul>
        <li> Sylvain Beucler
        <li> Uyjulian
        <li> Xavimat
        <li> Zedraxlo
        <li> 被诅咒的章鱼
        <li> 逆转咸鱼
    </ul><td></tr></table>

everyone who's tested this release, and myself, Tom "PyTom" Rothamel.
""",
    history="""\
""",

    full_html="""\
""",

    top_html="""\
""",
)

Release(
    prerelease=False,
    invisible=False,
    version="7.4.9",
    pygame="-2.1.0",
    date="October 7, 2021",
    patch=None,
    name="Lucky Robot Retcon",
    world_order=11,
    announcement="""\
I'd like to announce Ren'Py 7.4.9, the ninth patch release of Ren'Py
7.4. The largest amount of work was done to update the Android version
of Ren'Py to keep pace with Google Play's requirements. Ren'Py now
uses the Android App Bundle format, and uses Play Asset Delivery
to download assets to the player's device.

In addition to the Android improvements, some of the major changes are:

* The iOS version of Ren'Py now produces more complete projects, requiring
  less work to get projects working.
* Improvements to the web updater, providing a less efficient mode
  that works with https web servers.
* A new option in the launcher that can tell you if a new Ren'Py release
  exists.
* Improvements to the 3D stage, so that the camera statement and perspective
  work with transitions and transforms.
* Transforms now can take fractional sizes.
* The shift+A accessibility menu now has a new high-contrast mode, to make
  text more readable.

These are just some of the improvements in this release, so please read
the changelog to find everything new.

Ren'Py 7.4 is brought to you by:

.. raw:: html

    <table style="width: 100%;">
    <tr>
    <td style="width: 25%; vertical-align: top">
    <ul>
        <li> Andrej
        <li> Andrí Wilford
        <li> Andy_kl
        <li> Capntrips
        <li> Charles Surett
        <li> Cherie Davidson
        <li> CobaltCore
        <li> CodePsy
        <li> Daniel Conley
        <li> Daniel Luque
        <li> Dogtopus
        <li> Eric Ahn
        <li> GanstaKingofSA
        <li> GimmiRuski
        <li> GiovanH
        <li> Gouvernathor
    </ul></td><td style="width: 25%; vertical-align: top"><ul>
        <li> Gratusfr
        <li> Hanaka
        <li> Hyper Sonic
        <li> Jackmcbarn
        <li> Jan Masek
        <li> Joaquin Garmendia Cabrera
        <li> Joshua Fehler
        <li> Joshua Stone
        <li> Jürg Billeter
        <li> Kapil Gain
        <li> KG
        <li> Kyouryuukunn
        <li> Lee Yunseok
        <li> Lent1
        <li> Lezalith
        <li> Liu Wenyuan
    </ul></td><td style="width: 25%; vertical-align: top"><ul>
        <li> Lucas Ramage
        <li> Maciej Katafiasz
        <li> Mal Graty
        <li> Mason Chou
        <li> Maxwell Paul Brickner
        <li> Midgethetree
        <li> Moshibit
        <li> Neotus
        <li> Neyunse
        <li> Paul J Martinez
        <li> Remix
        <li> Ruben Jesus Garcia-Hernandez
        <li> Siege-Wizard
        <li> Shawna-p
        <li> Sylvain Beucler
    </ul></td><td style="width: 25%; vertical-align: top"><ul>
        <li> Uyjulian
        <li> Xavimat
        <li> Zedraxlo
        <li> 被诅咒的章鱼
        <li> 逆转咸鱼
    </ul><td></tr></table>

everyone who's tested this release, and myself, Tom "PyTom" Rothamel.
""",
    history="""\
""",

    full_html="""\
""",

    top_html="""\
""",
)

Release(
    prerelease=False,
    invisible=False,
    version="7.4.8",
    pygame="-2.1.0",
    date="August 2, 2021",
    patch=None,
    name="Lucky Eight Ball",
    world_order=11,
    announcement="""\
I'd like to announce Ren'Py 7.4.8, the eighth patch release of Ren'Py
7.4. This release is focused on fixes, and especially fixes a problem
introduced in Ren'Py 7.4.7 that could, in some circumstances, cause
data to become corrupt during rollback.

Everyone on 7.4.7 should upgrade.

In addition to that fix, there are multiple other fixes, and a
single new feature - the ability to pause playing movies like
any other sound channel. Please see the changelog for a complete
list of what has changed.

Ren'Py 7.4 is the the product of over a year of
development, and one of the biggest releases of Ren'Py to date. This
series of releases focuses on updating Ren'Py's internals so that Ren'Py
is ready for its next 15 years.

Ren'Py 7.4 is brought to you by:

* Andrej
* Andrí Wilford
* Andy_kl
* Capntrips
* Cherie Davidson
* CobaltCore
* CodePsy
* Daniel Conley
* Daniel Luque
* Dogtopus
* Eric Ahn
* GimmiRuski
* Gio
* Gouvernathor
* Gratusfr
* Hyper Sonic
* Jackmcbarn
* Jan Masek
* Joaquin Garmendia Cabrera
* Joshua Fehler
* Joshua Stone
* Kapil Gain
* KG
* Kyouryuukunn
* Lee Yunseok
* Lent1
* Lezalith
* Lucas Ramage
* Maciej Katafiasz
* Mal Graty
* Mason Chou
* Maxwell Paul Brickner
* Midgethetree
* Moshibit
* Neotus
* Paul J Martinez
* Remix
* Ruben Jesus Garcia-Hernandez
* Siege-Wizard
* Shawna-p
* Sylvain Beucler
* Uyjulian
* Xavimat
* Zedraxlo
* 被诅咒的章鱼
* 逆转咸鱼

everyone who's tested this release, and myself, Tom "PyTom" Rothamel.
""",
    history="""\
""",

    full_html="""\
""",

    top_html="""\
""",
)

Release(
    prerelease=False,
    invisible=False,
    version="7.4.7",
    pygame="-2.1.0",
    date="July 13, 2021",
    patch=None,
    name="The Queen of the Skies",
    world_order=11,
    announcement="""\
I'm happy to announce Ren'Py 7.4.7, the seventh patch release of Ren'Py
7.4. This release includes many fixes, and some major improvements.

Perhaps the biggest set of changes was to the Web port of Ren'Py, which
has been rewritten to use the web browser's native audio processing. This
prevents expensive operations, like decoding image files, from interrupting
audio playback. (However, an issue with Safari still exists.) Self-voicing
has also been added to the web plaform.

There have also been improvements to support for the iOS platform, that allow
Ren'Py games to run on the latest iPhones without aggressive pillarboxing.

The input displayable has grown quite a bit of functionality, with more
keys being supported, and the caret blinking to indicate that text can
be edited.

The Atom editor has been updated.

There is quite a bit of new functionality in this release, please check out
the changelog for some of the new things that can be done.

Ren'Py 7.4 is the the product of over a year of
development, and one of the biggest releases of Ren'Py to date. This
series of releases focuses on updating Ren'Py's internals so that Ren'Py
is ready for its next 15 years.

Ren'Py 7.4 is brought to you by:

* Andrej
* Andrí Wilford
* Andy_kl
* Capntrips
* Cherie Davidson
* CobaltCore
* CodePsy
* Daniel Conley
* Daniel Luque
* Dogtopus
* Eric Ahn
* GimmiRuski
* Gio
* Gouvernathor
* Gratusfr
* Hyper Sonic
* Jackmcbarn
* Jan Masek
* Joaquin Garmendia Cabrera
* Joshua Fehler
* Joshua Stone
* Kapil Gain
* KG
* KorDen
* Kyouryuukunn
* Lee Yunseok
* Lent1
* Lezalith
* Lucas Ramage
* Maciej Katafiasz
* Mal Graty
* Mason Chou
* Maxwell Paul Brickner
* Meithal
* Midgethetree
* Moshibit
* Neotus
* Paul J Martinez
* Remix
* Ruben Jesus Garcia-Hernandez
* Siege-Wizard
* Shawna-p
* Sylvain Beucler
* Uyjulian
* Xavimat
* Zedraxlo
* 被诅咒的章鱼
* 逆转咸鱼

everyone who's tested this release, and myself, Tom "PyTom" Rothamel.
""",
    history="""\
""",

    full_html="""\
""",

    top_html="""\
""",
)

Release(
    prerelease=False,
    invisible=False,
    version="7.4.6",
    pygame="-2.1.0",
    date="June 13, 2021",
    patch=None,
    name="Lucky Dice",
    world_order=11,
    announcement="""\
I'm happy to announce Ren'Py 7.4.6, the sixth patch release for the 7.4
series. This release contains a number of fixes for  7.4.5, both to improve
platform compatibility and to extend some to the features added for the
new 3D Stage.

This release include a new camera statement, which is used to introduce
transforms that will persist until changed. This allows the show layer
statement to revert to the behavior it had in 7.4.4, improving compatibility
with projects in production. At the same time, it allows more concise control
of the camera in 3D productions.

This release introduces the Model displayable. While right now focused on
allowing multiple textures to be combined (it's now possible to implement
dissolve-like transforms without a creator-defined displayable), it will
in the future serve as a way to access 2D and 3D model functionality.

This release fixes a mistake in the 7.4.5 that prevented builds from working
on iOS, and gets the model-based renderer working on that platform.

This release updates Atom and the language-renpy plugin.

In addition, there are a number of bug fixes and other improvements.

Ren'Py 7.4 is the the product of over a year of
development, and one of the biggest releases of Ren'Py to date. This
series of releases focuses on updating Ren'Py's internals so that Ren'Py
is ready for its next 15 years.

Ren'Py 7.4 is brought to you by:

* Andrej
* Andrí Wilford
* Andy_kl
* Capntrips
* Cherie Davidson
* CobaltCore
* CodePsy
* Daniel Conley
* Daniel Luque
* Dogtopus
* Eric Ahn
* GimmiRuski
* Gio
* Gouvernathor
* Gratusfr
* Hyper Sonic
* Jackmcbarn
* Jan Masek
* Joaquin Garmendia Cabrera
* Joshua Fehler
* Joshua Stone
* Kapil Gain
* KG
* Kyouryuukunn
* Lee Yunseok
* Lent1
* Lezalith
* Lucas Ramage
* Maciej Katafiasz
* Mal Graty
* Mason Chou
* Maxwell Paul Brickner
* Midgethetree
* Moshibit
* Neotus
* Paul J Martinez
* Remix
* Shawna-p
* Sylvain Beucler
* Uyjulian
* Xavimat
* Zedraxlo
* 被诅咒的章鱼
* 逆转咸鱼

everyone who's tested this release, and myself, Tom "PyTom" Rothamel.
""",
    history="""\
""",

    full_html="""\
""",

    top_html="""\
""",
)

Release(
    prerelease=False,
    invisible=False,
    version="7.4.5",
    pygame="-2.1.0",
    date="May 26, 2021",
    patch=None,
    name="The Five-Leaf Clover",
    world_order=11,
    announcement="""\
I'm happy to announce Ren'Py 7.4.5, the fifth patch release for the 7.4
series. This fix adds several features that take advantage of the
model-based renderer, improves platform support, and adds other
quality of life features, like a dark theme for the launcher.

Perhaps the biggest new feature is the 3D Stage system. This allows a
creator to position images on a three dimensional stage, like the one
a play takes place on. Images can be rotated and moved in three dimensions,
and Ren'Py will take care of rendering them in a perspective-correct manner.

Other features that take advantage of the model-based renderer are
new blend modes (including multiply), and a new transition, Swing,
that rotates images in three dimensions. The model-based renderer
is enabled by default in games released with Ren'Py 7.4.5.

This release also includes improvements for many platforms. The Android
support allows new projects to be compiled after the bintray shutdown,
while a rewritten splashscreen allows Ren'Py to start on more devices.
This release also includes fixes for compiling on iOS, and for signing
and notarizing macOS applications.

Ren'Py 7.4 is the the product of over a year of
development, and one of the biggest releases of Ren'Py to date. This
series of releases focuses on updating Ren'Py's internals so that Ren'Py
is ready for its next 15 years.

Ren'Py 7.4 is brought to you by:

* Andrej
* Andrí Wilford
* Andy_kl
* Capntrips
* Cherie Davidson
* CobaltCore
* CodePsy
* Daniel Conley
* Daniel Luque
* Dogtopus
* Eric Ahn
* GimmiRuski
* Gio
* Gouvernathor
* Gratusfr
* Hyper Sonic
* Jackmcbarn
* Jan Masek
* Joaquin Garmendia Cabrera
* Joshua Fehler
* Joshua Stone
* Kapil Gain
* KG
* Kyouryuukunn
* Lee Yunseok
* Lent1
* Lezalith
* Lucas Ramage
* Maciej Katafiasz
* Mal Graty
* Mason Chou
* Maxwell Paul Brickner
* Midgethetree
* Moshibit
* Neotus
* Paul J Martinez
* Remix
* Shawna-p
* Sylvain Beucler
* Uyjulian
* Xavimat
* Zedraxlo
* 被诅咒的章鱼
* 逆转咸鱼

everyone who's tested this release, and myself, Tom "PyTom" Rothamel.
""",
    history="""\
""",

    full_html="""\
""",

    top_html="""\
""",
)

Release(
    prerelease=False,
    invisible=False,
    version="7.4.4",
    pygame="-2.1.0",
    date="March 17, 2021",
    patch=None,
    name="The Pot of Gold",
    world_order=11,
    announcement="""\
I'm happy to announce Ren'Py 7.4.4, the fourth patch release for the 7.4
series. This fixes a pair of regressions, one that stopped the Web Beta
from working, and another that prevented gestures and controller support
from working.

This release adds basic support for custom blend modes, and uses that
support to implement additive and multiplicative blends for Live2D.
It also fixes an issue with large textures that usually manifested
as problems with Live2D.

It also includes a new feature that makes it possible to supply old
.rpyc files to Ren'Py, which should help maintain save compatibility
with games that are released more than once, such as games with
early access.

Everyone should upgrade.

Ren'Py 7.4 is the the product of over a year of
development, and one of the biggest releases of Ren'Py to date. This
series of releases focuses on updating Ren'Py's internals so that Ren'Py
is ready for its next 15 years.

Some of the bigger changes are:

* A new model-based renderer. While this is opt-in for the moment, it
  opens the way to features that creators have been requesting for a
  long time, such as being able to recolor displayables, blurring the
  screen, and using Live2D to animate sprites. The model-based renderer
  is extensible with shaders, allowing for custom effects.
* A new Python 3 compatibility mode has been added, to pave the way for Python 3
  support in the next release. This mode changes the ways in which Ren'Py
  runs, to allow you to begin porting your game before full Python 3
  comes out in Ren'Py 8.0.
* Ren'Py's build system has been modernized, and the libraries underlying it
  have been updated. This allows 64-bit Windows to be supported.
* The web platform has been updated, to allow for the incremental download
  of games.

This release also raises the minimum requirements to run a Ren'Py game. It is
now required that a user's computer have OpenGL 2, DirectX 9, OpenGL ES 2,
or WebGL to run Ren'Py. The model-based renderer requires OpenGL ES 3 or WebGL 2.

With these changes, there have been a few deprecations. Ren'Py no longer runs
on Windows XP. The minimum version of macOS Ren'Py supports is now 10.10.
The 32-bit armv7l platform has been removed on iOS, as this platform hasn't been supported
by Apple for several years. The Editra text editor has been removed, as
it hasn't been supported for quite some time, and wasn't compatible with
the new build system.

It's my hope that this release will enable creators to take on projects
they couldn't before, and will provide a solid basis for the next releases
of Ren'Py.

Ren'Py 7.4 is brought to you by:

* Andrej
* Andrí Wilford
* Andy_kl
* Capntrips
* Cherie Davidson
* CobaltCore
* Daniel Conley
* Daniel Luque
* Dogtopus
* Eric Ahn
* GimmiRuski
* Gio
* Gouvernathor
* Gratusfr
* Hyper Sonic
* Jackmcbarn
* Jan Masek
* Joaquin Garmendia Cabrera
* Joshua Fehler
* Joshua Stone
* Kapil Gain
* Kyouryuukunn
* Lee Yunseok
* Lezalith
* Lucas Ramage
* Maciej Katafiasz
* Mal Graty
* Mason Chou
* Maxwell Paul Brickner
* Midgethetree
* Moshibit
* Neotus
* Paul J Martinez
* Remix
* Shawna-p
* Sylvain Beucler
* Uyjulian
* Xavimat
* Zedraxlo
* 被诅咒的章鱼
* 逆转咸鱼

everyone who's tested this release, and myself, Tom "PyTom" Rothamel.
""",
    history="""\
""",

    full_html="""\
""",

    top_html="""\
""",
)

Release(
    prerelease=False,
    invisible=False,
    version="7.4.3",
    pygame="-2.1.0",
    date="March 8, 2021",
    patch=None,
    name="The Best One",
    world_order=11,
    announcement="""\
I'm happy to announce Ren'Py 7.4.3, the third patch release for the 7.4
series. This release improves the compatibility of Ren'Py 7.4, and adds
some new features. New to Ren'Py 7.4.3 are:

* Windows improvements that should increase compatibility and reduce the
  chance of false positives from some antivirus software.
* Improved compatibility with Android devices.
* A number of focus improvements, including marking frames modal, and
  focusing the mask part of an AlphaMask.
* The ability to render Emoji found in fonts.

This release includes feature improvements and updates translations.
Everyone should upgrade.

Ren'Py 7.4 is the the product of over a year of
development, and one of the biggest releases of Ren'Py to date. This
series of releases focuses on updating Ren'Py's internals so that Ren'Py
is ready for its next 15 years.

Some of the bigger changes are:

* A new model-based renderer. While this is opt-in for the moment, it
  opens the way to features that creators have been requesting for a
  long time, such as being able to recolor displayables, blurring the
  screen, and using Live2D to animate sprites. The model-based renderer
  is extensible with shaders, allowing for custom effects.
* A new Python 3 compatibility mode has been added, to pave the way for Python 3
  support in the next release. This mode changes the ways in which Ren'Py
  runs, to allow you to begin porting your game before full Python 3
  comes out in Ren'Py 8.0.
* Ren'Py's build system has been modernized, and the libraries underlying it
  have been updated. This allows 64-bit Windows to be supported.
* The web platform has been updated, to allow for the incremental download
  of games.

This release also raises the minimum requirements to run a Ren'Py game. It is
now required that a user's computer have OpenGL 2, DirectX 9, OpenGL ES 2,
or WebGL to run Ren'Py. The model-based renderer requires OpenGL ES 3 or WebGL 2.

With these changes, there have been a few deprecations. Ren'Py no longer runs
on Windows XP. The minimum version of macOS Ren'Py supports is now 10.10.
The 32-bit armv7l platform has been removed on iOS, as this platform hasn't been supported
by Apple for several years. The Editra text editor has been removed, as
it hasn't been supported for quite some time, and wasn't compatible with
the new build system.

It's my hope that this release will enable creators to take on projects
they couldn't before, and will provide a solid basis for the next releases
of Ren'Py.

Ren'Py 7.4 is brought to you by:

* Andrej
* Andrí Wilford
* Andy_kl
* Capntrips
* Cherie Davidson
* CobaltCore
* Daniel Conley
* Daniel Luque
* Dogtopus
* Eric Ahn
* GimmiRuski
* Gio
* Gouvernathor
* Gratusfr
* Hyper Sonic
* Jackmcbarn
* Jan Masek
* Joaquin Garmendia Cabrera
* Joshua Fehler
* Joshua Stone
* Kapil Gain
* Kyouryuukunn
* Lee Yunseok
* Lezalith
* Lucas Ramage
* Maciej Katafiasz
* Mal Graty
* Mason Chou
* Maxwell Paul Brickner
* Midgethetree
* Moshibit
* Neotus
* Paul J Martinez
* Remix
* Shawna-p
* Sylvain Beucler
* Uyjulian
* Xavimat
* Zedraxlo
* 被诅咒的章鱼
* 逆转咸鱼

everyone who's tested this release, and myself, Tom "PyTom" Rothamel.
""",
    history="""\
""",

    full_html="""\
""",

    top_html="""\
""",
)

Release(
    prerelease=False,
    invisible=False,
    version="7.4.2",
    pygame="-2.1.0",
    date="January 31, 2021",
    patch=None,
    name="The Betterer One",
    world_order=11,
    announcement="""\
I'm happy to announce Ren'Py 7.4.2, the second patch release for the 7.4
series. This release fixes a number of issues found in Ren'Py 7.4, including
some that only affect users that need accessibility options. Everyone should upgrade.

Ren'Py 7.4 is the the product of over a year of
development, and one of the biggest releases of Ren'Py to date. This
series of releases focuses on updating Ren'Py's internals so that Ren'Py
is ready for its next 15 years.

Some of the bigger changes are:

* A new model-based renderer. While this is opt-in for the moment, it
  opens the way to features that creators have been requesting for a
  long time, such as being able to recolor displayables, blurring the
  screen, and using Live2D to animate sprites. The model-based renderer
  is extensible with shaders, allowing for custom effects.
* A new Python 3 compatibility mode has been added, to pave the way for Python 3
  support in the next release. This mode changes the ways in which Ren'Py
  runs, to allow you to begin porting your game before full Python 3
  comes out in Ren'Py 8.0.
* Ren'Py's build system has been modernized, and the libraries underlying it
  have been updated. This allows 64-bit Windows to be supported.
* The web platform has been updated, to allow for the incremental download
  of games.

This release also raises the minimum requirements to run a Ren'Py game. It is
now required that a user's computer have OpenGL 2, DirectX 9, OpenGL ES 2,
or WebGL to run Ren'Py. The model-based renderer requires OpenGL ES 3 or WebGL 2.

With these changes, there have been a few deprecations. Ren'Py no longer runs
on Windows XP. The minimum version of macOS Ren'Py supports is now 10.10.
The 32-bit armv7l platform has been removed on iOS, as this platform hasn't been supported
by Apple for several years. The Editra text editor has been removed, as
it hasn't been supported for quite some time, and wasn't compatible with
the new build system.

It's my hope that this release will enable creators to take on projects
they couldn't before, and will provide a solid basis for the next releases
of Ren'Py.

Ren'Py 7.4 is brought to you by:

* Andrej
* Andrí Wilford
* Andy_kl
* Capntrips
* Cherie Davidson
* CobaltCore
* Daniel Conley
* Daniel Luque
* Dogtopus
* Eric Ahn
* GimmiRuski
* Gio
* Gouvernathor
* Gratusfr
* Hyper Sonic
* Jackmcbarn
* Jan Masek
* Joaquin Garmendia Cabrera
* Joshua Fehler
* Joshua Stone
* Kapil Gain
* Kyouryuukunn
* Lee Yunseok
* Lezalith
* Lucas Ramage
* Maciej Katafiasz
* Mal Graty
* Mason Chou
* Maxwell Paul Brickner
* Midgethetree
* Moshibit
* Neotus
* Paul J Martinez
* Remix
* Shawna-p
* Sylvain Beucler
* Uyjulian
* Xavimat
* Zedraxlo
* 被诅咒的章鱼
* 逆转咸鱼

everyone who's tested this release, and myself, Tom "PyTom" Rothamel.
""",
    history="""\
Ren'Py 7.4.1 is the first patch release, addressing bugs and compatibility
issues found in Ren'Py 7.4.0. As some of these issues may affect end-users
of games without affecting creators, everyone is encouraged to upgrade as
soon as possible.
""",

    full_html="""\
""",

    top_html="""\
""",
)

Release(
    prerelease=False,
    invisible=False,
    version="7.4.1",
    pygame="-2.1.0",
    date="January 23, 2021",
    patch=None,
    name="The Better One",
    world_order=11,
    announcement="""\
I'm happy to announce Ren'Py 7.4.1, the first patch release for the 7.4
series. This release fixes a number of issues found in Ren'Py 7.4.0.
Everyone should upgrade.

Ren'Py 7.4 is the the product of over a year of
development, and one of the biggest releases of Ren'Py to date. This
series of releases focuses on updating Ren'Py's internals so that Ren'Py
is ready for its next 15 years.

Some of the bigger changes are:

* A new model-based renderer. While this is opt-in for the moment, it
  opens the way to features that creators have been requesting for a
  long time, such as being able to recolor displayables, blurring the
  screen, and using Live2D to animate sprites. The model-based renderer
  is extensible with shaders, allowing for custom effects.
* A new Python 3 compatibility mode has been added, to pave the way for Python 3
  support in the next release. This mode changes the ways in which Ren'Py
  runs, to allow you to begin porting your game before full Python 3
  comes out in Ren'Py 8.0.
* Ren'Py's build system has been modernized, and the libraries underlying it
  have been updated. This allows 64-bit Windows to be supported.
* The web platform has been updated, to allow for the incremental download
  of games.

This release also raises the minimum requirements to run a Ren'Py game. It is
now required that a user's computer have OpenGL 2, DirectX 9, OpenGL ES 2,
or WebGL to run Ren'Py. The model-based renderer requires OpenGL ES 3 or WebGL 2.

With these changes, there have been a few deprecations. Ren'Py no longer runs
on Windows XP. The minimum version of macOS Ren'Py uspports is now 10.10.
The 32-bit armv7l platform has been removed on iOS, as this platform hasn't been supported
by Apple for several years. The Editra text editor has been removed, as
it hasn't been supported for quite some time, and wasn't compatible with
the new build system.

It's my hope that this release will enable creators to take on projects
they couldn't before, and will provide a solid basis for the next releases
of Ren'Py.

Ren'Py 7.4 is brought to you by:

* Andrej
* Andy_kl
* Capntrips
* Cherie Davidson
* CobaltCore
* Daniel Conley
* Daniel Luque
* Dogtopus
* Eric Ahn
* GimmiRuski
* Gio
* Gouvernathor
* Gratusfr
* Hyper Sonic
* Jackmcbarn
* Joaquin Garmendia Cabrera
* Joshua Fehler
* Joshua Stone
* Kapil Gain
* Kyouryuukunn
* Lee Yunseok
* Lezalith
* Lucas Ramage
* Maciej Katafiasz
* Mal Graty
* Mason Chou
* Maxwell Paul Brickner
* Moshibit
* Neotus
* Paul J Martinez
* Remix
* Shawna-p
* Sylvain Beucler
* Uyjulian
* Zedraxlo

everyone who's tested this release, and myself, Tom "PyTom" Rothamel.
""",
    history="""\
Ren'Py 7.4.1 is the first patch release, addressing bugs and compatibility
issues found in Ren'Py 7.4.0. As some of these issues may affect end-users
of games without affecting creators, everyone is encouraged to upgrade as
soon as possible.
""",

    full_html="""\
""",

    top_html="""\
""",
)

Release(
    prerelease=False,
    invisible=False,
    version="7.4.0",
    pygame="-2.1.0",
    date="December 31, 2020",
    patch=None,
    name="The Big One",
    world_order=11,
    announcement="""\
I'm happy to announce Ren'Py 7.4, the product of over a year of
development, and one of the biggest releases of Ren'Py to date. This
release focuses on updating Ren'Py's internals so that Ren'Py is ready
for its next 15 years.

Some of the bigger changes are:

* A new model-based renderer. While this is opt-in for the moment, it
  opens the way to features that creators have been requesting for a
  long time, such as being able to recolor displayables, blurring the
  screen, and using Live2D to animate sprites. The model-based renderer
  is extensible with shaders, allowing for custom effects.
* A new Python 3 compatibility mode has been added, to pave the way for Python 3
  support in the next release. This mode changes the ways in which Ren'Py
  runs, to allow you to begin porting your game before full Python 3
  comes out in Ren'Py 8.0.
* Ren'Py's build system has been modernized, and the libraries underlying it
  have been updated. This allows 64-bit Windows to be supported.
* The web platform has been updated, to allow for the incremental download
  of games.

This release also raises the minimum requirements to run a Ren'Py game. It is
now required that a user's computer have OpenGL 2, DirectX 9, OpenGL ES 2,
or WebGL to run Ren'Py. The model-based renderer requires OpenGL ES 3 or WebGL 2.

With these changes, there have been a few deprecations. Ren'Py no longer runs
on Windows XP. The 32-bit armv7l
platform has been removed on iOS, as this platform hasn't been supported
by Apple for several years. The Editra text editor has been removed, as
it hasn't been supported for quite some time, and wasn't compatible with
the new build system.

It's my hope that this release will enable creators to take on projects
they couldn't before, and will provide a solid basis for the next releases
of Ren'Py.

Ren'Py 7.4 is brought to you by:

* Andrej
* Andy_kl
* Capntrips
* Cherie Davidson
* CobaltCore
* Daniel Conley
* Daniel Luque
* Dogtopus
* Eric Ahn
* GimmiRuski
* Gio
* Gouvernathor
* Gratusfr
* Hyper Sonic
* Jackmcbarn
* Joaquin Garmendia Cabrera
* Joshua Fehler
* Joshua Stone
* Kapil Gain
* Kyouryuukunn
* Lee Yunseok
* Lezalith
* Lucas Ramage
* Maciej Katafiasz
* Mal Graty
* Mason Chou
* Maxwell Paul Brickner
* Moshibit
* Neotus
* Paul J Martinez
* Remix
* Shawna-p
* Sylvain Beucler
* Uyjulian
* Zedraxlo

everyone who's tested this release, and myself, Tom "PyTom" Rothamel.
""",
    history="""\
""",

    full_html="""\
""",

    top_html="""\
""",
)

Release(
    prerelease=False,
    invisible=False,
    version="7.3.5",
    pygame="-2.1.0",
    date="October 17, 2019",
    patch=None,
    name="The world (wide web) is not enough.",
    world_order=10,
    announcement="""\
I'm happy to announce Ren'Py 7.3.5, the latest in a series of
releases that continue to maintain Ren'Py 7.3. This release fixes the
compilation of iOS projects, and adds a button that accesses the audio
directory to the launcher.

As there have been quite a few changes since Ren'Py 7.3 was originally
released, please check out the changelog for new features that will help
you create your visual novels and games.

Ren'Py 7.3 is brought to you by:

* Alisha Taylor
* Andy_kl
* Arda Güler
* Ben Wright
* DragoonHP
* Donghyeok Tak
* Herpior
* Jan Beich
* Joshua Fehler
* Julian Uy
* Kobaltcore
* Lee Yunseok
* Mal Graty
* Moshibit
* Nyaatrap
* Pionere
* Psunbury
* Remix
* Roope Herpiö
* Sylvain Beucler

and myself, Tom "PyTom" Rothamel.
""",
    history="""\
There has been an update to Ren'Py 7.3.5 to address the requirement
that Android applications target Android 10 (android-29). For a
link and instructions on how to install this update, please see
the `thread on the Lemma Soft Forums <https://lemmasoft.renai.us/forums/viewtopic.php?t=59848>`_.
""",

    full_html="""\
<img src="/static/7.2.0.jpg" alt="" style="width: 100%">
""",

    top_html="""\
""",
)

Release(
    prerelease=False,
    invisible=False,
    version="7.3.4",
    pygame="-2.1.0",
    date="October 8, 2019",
    patch=None,
    name="The world (wide web) is not enough.",
    world_order=10,
    announcement="""\
I'm happy to announce Ren'Py 7.3.4, a further patch to Ren'Py 7.3. This
fixes two major graphical glitches, and also adds the ability to pass
"[prefix_]" to image names everywhere, rather than only in styles.

Ren'Py 7.3.3 was intended to improve performance and compatibility,
fix bugs, and make available minor features
that have been added since Ren'Py 7.3.2 was released.

Some highlights are:

* An audio directory that allows audio files to define themselves, similar
  to images.
* The ability for Ren'Py to accept audio files generated at runtime.
* A lowering of the version of android needed to run Ren'Py.
* Many improvements to Web platform support.
* Improved render-to-texture performance.
* The ability of renpy.input to take custom screens.
* Ren'Py is now signed and notarized to run on macOS.

Ren'Py 7.3.2 is a patch release to Ren'Py
7.3, mostly intended to fix bugs and address issues that people have
reported. As some of the bugs have significant performance and correctness
impact, everyone who upgraded to Ren'Py 7.3.0 or 7.3.1 should move on to this version.

Ren'Py 7.3.1 added a few minor new features, including the ability to
customize descriptive text.

Ren'Py 7.3 is the first release of
Ren'Py with support for running on the web platform, inside a web browser
supporting HTML 5, Web Assembly, and WebGL. Right now, this support is in
beta, as it's limited by the capabilities of the web platform itself, but
it's suitable for making web demos of Ren'Py games.

In addition to that, this release adds many new features to Ren'Py. These
include:

* Many improvements to creator-defined statements, allowing the parsing
  of Ren'Py statements and block, the catching of errors, and the ability
  to execute a second function after Ren'Py in the body of a statement
  has finished.
* Screen language improvements, like the ability to capture screen language
  displayables into a variable and to use a property to determine if a screen
  is sensitive to input.
* Text improvements, with self-closing text tags and the ability to control
  the capitalization of interpolated text.
* Mobile platforms now support non-rectangular focus masks, and 64-bit Android
  is supported in time for the Google Play deadline.
* There is a new Turkish translation of the launcher and Spanish translation of
  the tutorial game, while several of the other translations have been updated.

There are also a number of other changes, so check out the changelog for all
of what's new.

Ren'Py 7.3 is brought to you by:

* Alisha Taylor
* Andy_kl
* Arda Güler
* Ben Wright
* DragoonHP
* Donghyeok Tak
* Herpior
* Jan Beich
* Joshua Fehler
* Julian Uy
* Kobaltcore
* Lee Yunseok
* Mal Graty
* Moshibit
* Nyaatrap
* Pionere
* Psunbury
* Remix
* Roope Herpiö
* Sylvain Beucler

and myself, Tom "PyTom" Rothamel.
""",
    history="""\
""",

    full_html="""\
<img src="/static/7.2.0.jpg" alt="" style="width: 100%">
""",

    top_html="""\
""",
)

Release(
    prerelease=False,
    invisible=False,
    version="7.3.3",
    pygame="-2.1.0",
    date="October 1, 2019",
    patch=None,
    name="The world (wide web) is not enough.",
    world_order=10,
    announcement="""\
I'm happy to announce Ren'Py 7.3.3. This release is intended to improve
performance and compatibility, fix bugs, and make available minor features
that have been added since Ren'Py 7.3.2 was released.

Some highlights are:

* An audio directory that allows audio files to define themselves, similar
  to images.
* The ability for Ren'Py to accept audio files generated at runtime.
* A lowering of the version of android needed to run Ren'Py.
* Many improvements to Web platform support.
* Improved render-to-texture performance.
* The ability of renpy.input to take custom screens.
* Ren'Py is now signed and notarized to run on macOS.

Ren'Py 7.3.2 is a patch release to Ren'Py
7.3, mostly intended to fix bugs and address issues that people have
reported. As some of the bugs have significant performance and correctness
impact, everyone who upgraded to Ren'Py 7.3.0 or 7.3.1 should move on to this version.

Ren'Py 7.3.1 added a few minor new features, including the ability to
customize descriptive text.

Ren'Py 7.3 is the first release of
Ren'Py with support for running on the web platform, inside a web browser
supporting HTML 5, Web Assembly, and WebGL. Right now, this support is in
beta, as it's limited by the capabilities of the web platform itself, but
it's suitable for making web demos of Ren'Py games.

In addition to that, this release adds many new features to Ren'Py. These
include:

* Many improvements to creator-defined statements, allowing the parsing
  of Ren'Py statements and block, the catching of errors, and the ability
  to execute a second function after Ren'Py in the body of a statement
  has finished.
* Screen language improvements, like the ability to capture screen language
  displayables into a variable and to use a property to determine if a screen
  is sensitive to input.
* Text improvements, with self-closing text tags and the ability to control
  the capitalization of interpolated text.
* Mobile platforms now support non-rectangular focus masks, and 64-bit Android
  is supported in time for the Google Play deadline.
* There is a new Turkish translation of the launcher and Spanish translation of
  the tutorial game, while several of the other translations have been updated.

There are also a number of other changes, so check out the changelog for all
of what's new.

Ren'Py 7.3 is brought to you by:

* Alisha Taylor
* Andy_kl
* Arda Güler
* Ben Wright
* DragoonHP
* Donghyeok Tak
* Herpior
* Jan Beich
* Joshua Fehler
* Julian Uy
* Kobaltcore
* Lee Yunseok
* Mal Graty
* Moshibit
* Nyaatrap
* Pionere
* Psunbury
* Remix
* Roope Herpiö
* Sylvain Beucler

and myself, Tom "PyTom" Rothamel.
""",
    history="""\
""",

    full_html="""\
<img src="/static/7.2.0.jpg" alt="" style="width: 100%">
""",

    top_html="""\
""",
)

Release(
    prerelease=False,
    invisible=False,
    version="7.3.2",
    pygame="-2.1.0",
    date="July 1, 2019",
    patch=None,
    name="The world (wide web) is not enough.",
    world_order=10,
    announcement="""\
I'm mildly chagrined to announce Ren'Py 7.3.2. This is a patch release to Ren'Py
7.3, mostly intended to fix bugs and address issues that people have
reported. As some of the bugs have significant performance and correctness
impact, everyone who upgraded to Ren'Py 7.3.0 or 7.3.1 should move on to this version.

Ren'Py 7.3.1 added a few minor new features, including the ability to
customize descriptive text.

Ren'Py 7.3 is the first release of
Ren'Py with support for running on the web platform, inside a web browser
supporting HTML 5, Web Assembly, and WebGL. Right now, this support is in
beta, as it's limited by the capabilities of the web platform itself, but
it's suitable for making web demos of Ren'Py games.

In addition to that, this release adds many new features to Ren'Py. These
include:

* Many improvements to creator-defined statements, allowing the parsing
  of Ren'Py statements and block, the catching of errors, and the ability
  to execute a second function after Ren'Py in the body of a statement
  has finished.
* Screen language improvements, like the ability to capture screen language
  displayables into a variable and to use a property to determine if a screen
  is sensitive to input.
* Text improvements, with self-closing text tags and the ability to control
  the capitalization of interpolated text.
* Mobile platforms now support non-rectangular focus masks, and 64-bit Android
  is supported in time for the Google Play deadline.
* There is a new Turkish translation of the launcher and Spanish translation of
  the tutorial game, while several of the other translations have been updated.

There are also a number of other changes, so check out the changelog for all
of what's new.

Ren'Py 7.3 is brought to you by:

* Andy_kl
* Arda Güler
* DragoonHP
* Jan Beich
* Kobaltcore
* Lee Yunseok
* Mal Graty
* Moshibit
* Nyaatrap
* Pionere
* Sylvain Beucler

and myself, Tom "PyTom" Rothamel.
""",
    history="""\
""",

    full_html="""\
<img src="/static/7.2.0.jpg" alt="" style="width: 100%">
""",

    top_html="""\
""",
)

Release(
    prerelease=False,
    invisible=False,
    version="7.3.1",
    pygame="-2.1.0",
    date="July 1, 2019",
    patch=None,
    name="The world (wide web) is not enough.",
    world_order=10,
    announcement="""\
I'm happy to announce Ren'Py 7.3.1. This is a patch release to Ren'Py
7.3, mostly intended to fix bugs and address issues that people have
reported. As some of the bugs have significant performance and correctness
impact, everyone who upgraded to Ren'Py 7.3.0 should move on to this version.

Ren'Py 7.3.1 also adds a few minor new features.

Ren'Py 7.3 is the first release of
Ren'Py with support for running on the web platform, inside a web browser
supporting HTML 5, Web Assembly, and WebGL. Right now, this support is in
beta, as it's limited by the capabilities of the web platform itself, but
it's suitable for making web demos of Ren'Py games.

In addition to that, this release adds many new features to Ren'Py. These
include:

* Many improvements to creator-defined statements, allowing the parsing
  of Ren'Py statements and block, the catching of errors, and the ability
  to execute a second function after Ren'Py in the body of a statement
  has finished.
* Screen language improvements, like the ability to capture screen language
  displayables into a variable and to use a property to determine if a screen
  is sensitive to input.
* Text improvements, with self-closing text tags and the ability to control
  the capitalization of interpolated text.
* Mobile platforms now support non-rectangular focus masks, and 64-bit Android
  is supported in time for the Google Play deadline.
* There is a new Turkish translation of the launcher and Spanish translation of
  the tutorial game, while several of the other translations have been updated.

There are also a number of other changes, so check out the changelog for all
of what's new.

Ren'Py 7.3 is brought to you by:

* Andy_kl
* Arda Güler
* DragoonHP
* Jan Beich
* Kobaltcore
* Lee Yunseok
* Mal Graty
* Moshibit
* Nyaatrap
* Pionere
* Sylvain Beucler

and myself, Tom "PyTom" Rothamel.
""",
    history="""\
""",

    full_html="""\
<img src="/static/7.2.0.jpg" alt="" style="width: 100%">
""",

    top_html="""\
""",
)

Release(
    prerelease=False,
    invisible=False,
    version="7.3.0",
    pygame="-2.1.0",
    date="June 16, 2019",
    patch=None,
    name="The world (wide web) is not enough.",
    world_order=10,
    announcement="""\
I'm pleased to announce the release of Ren'Py 7.3.0, the first release of
Ren'Py with support for running on the web platform, inside a web browser
supporting HTML 5, Web Assembly, and WebGL. Right now, this support is in
beta, as it's limited by the capabilities of the web platform itself, but
it's suitable for making web demos of Ren'Py games.

In addition to that, this release adds many new features to Ren'Py. These
include:

* Many improvements to creator-defined statements, allowing the parsing
  of Ren'Py statements and block, the catching of errors, and the ability
  to execute a second function after Ren'Py in the body of a statement
  has finished.
* Screen language improvements, like the ability to capture screen language
  displayables into a variable and to use a property to determine if a screen
  is sensitive to input.
* Text improvements, with self-closing text tags and the ability to control
  the capitalization of interpolated text.
* Mobile platforms now support non-rectangular focus masks, and 64-bit Android
  is supported in time for the Google Play deadline.
* There is a new Turkish translation of the launcher and Spanish translation of
  the tutorial game, while several of the other translations have been updated.

There are also a number of other changes, so check out the changelog for all
of what's new.

Ren'Py 7.3.0 is brought to you by:

* Andy_kl
* Arda Güler
* DragoonHP
* Jan Beich
* Kobaltcore
* Lee Yunseok
* Mal Graty
* Moshibit
* Nyaatrap
* Pionere
* Sylvain Beucler

and myself, Tom "PyTom" Rothamel.
""",
    history="""\
""",

    full_html="""\
<img src="/static/7.2.0.jpg" alt="" style="width: 100%">
""",

    top_html="""\
""",
)

Release(
    prerelease=False,
    invisible=False,
    version="7.2.2",
    pygame="-2.1.0",
    date="March 31, 2019",
    patch=None,
    name="What's on the menu.",
    world_order=9,
    announcement="""\
Ren'Py 7.2.2 is out! This is mostly a patch release, but it also includes support
for the new accessibility menu, accessed by pressing 'a'. This menu puts current
and future engine-level accessibility features in one place.

Ren'Py 7.2 adds new features to Ren'Py, including:

* Menus now take arguments, and so do menu choices.
* The say statement can now take a temporary image attribute, making is
  possible to change a character's emotion for a single statement.
* The new im.Blur image manipulator can blur static images.
* Layeredimage groups can now contain non-conflicting attributes while
  still being automatically declared.
* It's possible to display a non-looping Movie displayable, and to have
  a movie display a static image before the first frame renders.
* A fullscreen Ren'Py will not minimize when the mouse changes monitors.
* Text now takes renpy.BASELINE as a yanchor, which allows one to position
  the text's baseline.
* The CTC screen now takes additional arguments, including the kind of
  click-to-continue indicator being shown.

Ren'Py 7.2 updates Ren'Py to work with the current Android SDK, and contains
a number of other bugfixes.

Ren'Py 7.2.2 is brought to you by:

* Andy_kl
* Craig P. Donson
* Eric Ahn
* Enerccio
* Frédéric Chapoton
* Mal Graty
* Meithal
* Moshibit
* Sergey Musiyenko
* Shayne Officer
* Sylvain Beucler
* Xavi-mat

and myself, Tom "PyTom" Rothamel.
""",
    history="""\
""",

    full_html="""\
<img src="/static/7.2.0.jpg" alt="" style="width: 100%">
""",

    top_html="""\
""",
)

Release(
    prerelease=False,
    invisible=False,
    version="7.2.1",
    pygame="-2.1.0",
    date="March 16, 2019",
    patch=None,
    name="What's on the menu.",
    world_order=9,
    announcement="""\
I'm happy to announce Ren'Py 7.2.1, a patch release. This release consists
primarily of fixes. It also adds support for generating the icon and
launchimage on iOS.

Ren'Py 7.2  adds new features to Ren'Py, including:

* Menus now take arguments, and so do menu choices.
* The say statement can now take a temporary image attribute, making is
  possible to change a character's emotion for a single statement.
* The new im.Blur image manipulator can blur static images.
* Layeredimage groups can now contain non-conflicting attributes while
  still being automatically declared.
* It's possible to display a non-looping Movie displayable, and to have
  a movie display a static image before the first frame renders.
* A fullscreen Ren'Py will not minimize when the mouse changes monitors.
* Text now takes renpy.BASELINE as a yanchor, which allows one to position
  the text's baseline.
* The CTC screen now takes additional arguments, including the kind of
  click-to-continue indicator being shown.

Ren'Py 7.2 updates Ren'Py to work with the current Android SDK, and contains
a number of other bugfixes.

Ren'Py 7.2.1 is brought to you by:

* Andy_kl
* Craig P. Donson
* Eric Ahn
* Enerccio
* Frédéric Chapoton
* Mal Graty
* Moshibit
* Sergey Musiyenko
* Shayne Officer
* Sylvain Beucler
* Xavi-mat

and myself, Tom "PyTom" Rothamel.
""",
    history="""\
""",

    full_html="""\
<img src="/static/7.2.0.jpg" alt="" style="width: 100%">
""",

    top_html="""\
""",
)

Release(
    prerelease=False,
    invisible=False,
    version="7.2.0",
    pygame="-2.1.0",
    date="March 3, 2019",
    patch=None,
    name="What's on the menu.",
    world_order=9,
    announcement="""\
I'm happy to announce Ren'Py 7.2.0. This release adds new features to
Ren'Py, including:

* Menus now take arguments, and so do menu choices.
* The say statement can now take a temporary image attribute, making is
  possible to change a character's emotion for a single statement.
* The new im.Blur image manipulator can blur static images.
* Layeredimage groups can now contain non-conflicting attributes while
  still being automatically declared.
* It's possible to display a non-looping Movie displayable, and to have
  a movie display a static image before the first frame renders.
* A fullscreen Ren'Py will not minimize when the mouse changes monitors.
* Text now takes renpy.BASELINE as a yanchor, which allows one to position
  the text's baseline.
* The CTC screen now takes additional arguments, including the kind of
  click-to-continue indicator being shown.

This release also updates Ren'Py to work with the current Android SDK, and contains
a number of other bugfixes.

Ren'Py 7.2.0 is brought to you by:

* Andy_kl
* Craig P. Donson
* Eric Ahn
* Mal Graty
* Moshibit
* Sergey Musiyenko
* Shayne Officer
* Sylvain Beucler
* Xavi-mat

and myself, Tom "PyTom" Rothamel.
""",
    history="""\
""",

    full_html="""\
<img src="/static/7.2.0.jpg" alt="" style="width: 100%">
""",

    top_html="""\
""",
)

Alias(old="7.1.4", new="7.2.0")

Release(
    prerelease=False,
    invisible=False,
    version="7.1.3",
    pygame="-2.1.0",
    date="November 18, 2018",
    patch=None,
    name="On the road again.",
    world_order=9,
    announcement="""\
I'm happy to announce Ren'Py 7.1.3. This is the third bug release for Ren'Py
7.1, which improves Ren'Py while fixing issues. (There was a language bug in
7.1.2 that necessitated a quick re-release. The rest of these notes apply
to 7.1.2.)

There have also been a few feature additions. Some of the highlights are:

* Transforms that are used once in a screen can now be defined inline.
* Choice menus can now display as insensitive buttons items selected by the
  if clause.
* It is now possible to set variables inside a used screen.
* Ren'Py can now automatically detect the language of the player's system
  and select the correct translation.
* The French, German, Korean, Russian, and Simplified Chinese translations
  have been updated.

Some of the more important bugfixes include:

* A bug that caused Arabic text to display as squares on Windows has been fixed.
* Lint now handles several cases correctly, including layered images.
* As Ren'Py generally could not created proper android packages with a 32-bit
  Java 8, it now requires a 64-bit Java Development Kit.

Ren'Py 7.1.3 is brought to you by:

* Alexandre-T
* Andy_kl
* Bryan Tsang
* Craig P. Donson
* Felix Lampe
* Joshua Fehler
* Konstantin Mozheyko
* Lee Yunseok
* Max le Fou
* Moshibit
* Muhammad Nur Hidayat Yasuyoshi
* Ria-kon
* Saltome
* Shehriyar Qureshi
* Sylvain Beucler
* nyaatraps
* philat
* Vollschauer
* Xavi-mat
* Xela
* Zedraxlo


and myself, Tom "PyTom" Rothamel.
""",
    history="""\
""",

    full_html="""\
<img src="/static/7.0.0.jpg" alt="" style="width: 100%">
""",

    top_html="""\
""",
)

Release(
    prerelease=False,
    invisible=False,
    version="7.1.2",
    pygame="-2.1.0",
    date="November 17, 2018",
    patch=None,
    name="On the road again.",
    world_order=9,
    announcement="""\
I'm happy to announce Ren'Py 7.1.2. This is the second bug release for Ren'Py
7.1, which improves Ren'Py while fixing issues.

There have also been a few feature additions. Some of the highlights are:

* Transforms that are used once in a screen can now be defined inline.
* Choice menus can now display as insensitive buttons items selected by the
  if clause.
* It is now possible to set variables inside a used screen.
* Ren'Py can now automatically detect the language of the player's system
  and select the correct translation.
* The French, German, Korean, Russian, and Simplified Chinese translations
  have been updated.

Some of the more important bugfixes include:

* A bug that caused Arabic text to display as squares on Windows has been fixed.
* Lint now handles several cases correctly, including layered images.
* As Ren'Py generally could not created proper android packages with a 32-bit
  Java 8, it now requires a 64-bit Java Development Kit.

Ren'Py 7.1.2 is brought to you by:

* Alexandre-T
* Andy_kl
* Bryan Tsang
* Craig P. Donson
* Felix Lampe
* Joshua Fehler
* Konstantin Mozheyko
* Lee Yunseok
* Max le Fou
* Moshibit
* Muhammad Nur Hidayat Yasuyoshi
* Ria-kon
* Saltome
* Shehriyar Qureshi
* Sylvain Beucler
* nyaatraps
* philat
* Vollschauer
* Xavi-mat
* Xela
* Zedraxlo


and myself, Tom "PyTom" Rothamel.
""",
    history="""\
""",

    full_html="""\
<img src="/static/7.0.0.jpg" alt="" style="width: 100%">
""",

    top_html="""\
""",
)

Release(
    prerelease=False,
    invisible=False,
    version="7.1.1",
    pygame="-2.1.0",
    date="October 10, 2018",
    patch=None,
    name="On the road again.",
    world_order=9,
    announcement="""\
I'm happy to announce Ren'Py 7.1.1. This is a bug release for Ren'Py
7.1, which improves the new android support and fixes a number of other
issues.

Some of the more important bugfixes include:

* A change to the History screen to fix problems with [[ in dialogue. (This
  requires you to change screens.rpy, see the changelog for details.)
* The Android SDK uses a sufficient amount of memory on low-memory computers.
* A problem with creating non-adaptive Android icons has been fixed.
* Zero-width characters are drawn correctly, and non-breaking spaces are
  respected in more places. (This fixes a problem with Arabic text rendering.)
* Automatic window management now considers dialogue and captions associated
  with the menu statement.

There have also been a few small feature additions:

* The SetVariable and ToggleVariable functions now can take namespaces,
  and fields, so it's posible to have actions like SetVariable("hero.strength", 42)
  and ToggleVariable("persistent.alternate_outfits").
* It is now possible to nestle the CTC indicator into the text in such a
  way that it can not be on a separate line from the final word of dialogue.
* Drags (used in drag-and-drop) now support alternate clicks, which are right
  clicks on PC and long-presses on touch platforms.
* The Russian and Korean translations have been updated.
* The 86_64 Android APK is given a different numeric version than the arm version,
  allowing both to be uploaded to the Play store.

Ren'Py 7.1.1 is brought to you by:

* Alexandre-T
* Andy_kl
* Andykl
* Bryan Tsang
* Craig P. Donson
* Joshua Fehler
* Lee Yunseok
* Max le Fou
* Moshibit
* Muhammad Nur Hidayat Yasuyoshi
* Ria-kon
* Saltome
* Sylvain Beucler
* nyaatraps
* philat
* xavi-mat


and myself, Tom "PyTom" Rothamel.
""",
    history="""\
""",

    full_html="""\
<img src="/static/7.0.0.jpg" alt="" style="width: 100%">
""",

    top_html="""\
""",
)

Release(
    prerelease=False,
    invisible=False,
    version="7.1.0",
    pygame="-2.1.0",
    date="September 10, 2018",
    patch=None,
    name="On the road again.",
    world_order=9,
    announcement="""\
I'm happy to announce Ren'Py 7.1.0. This release fixes issues with
Ren'Py 7.0.0, and also includes a few new features:

* Android support has been rewritten to use the modern gradle-based
  build system. This allows Android apps created using Ren'Py to
  be posted in the Google Play store again. This also improves them
  in other ways, like making the app smaller by splitting out support
  for different platforms.

* There is a new "monologue mode", which allows you to use triple-quoted
  strings to create say statements that contain multiple lines of dialogue.
  As part of this, the new {clear} text tag allows the equivalent of
  ``nvl clear`` to be embedded in dialogue.

* The new `_quit_slot` variable lets you specify a save slot that
  the game is saved to when the user quits.

* The updater (built into the launcher) has been updated to prompt for the
  channel to update to on each use, preventing creators from updated to
  an unexpected prerelease or nightly build.

As usual, check the changelog for a complete list of changes.

Ren'Py 7.1.0 is brought to you by:

* Alexandre-T
* Andy_kl
* Andykl
* Bryan Tsang
* Craig P. Donson
* Joshua Fehler
* Lee Yunseok
* Max le Fou
* Moshibit
* Muhammad Nur Hidayat Yasuyoshi
* Ria-kon
* Saltome
* Sylvain Beucler
* nyaatraps
* philat:
* xavi-mat

and myself, Tom "PyTom" Rothamel.
""",
    history="""\
""",

    full_html="""\
<img src="/static/7.0.0.jpg" alt="" style="width: 100%">
""",

    top_html="""\
""",
)

Release(
    prerelease=False,
    invisible=False,
    version="7.0",
    pygame="-2.1.0",
    date="June 01, 2018",
    patch=0,
    name="For all mankind.",
    world_order=9,
    announcement="""\
I'm happy to announce the release of Ren'Py 7, the result of over a decade
of development since Ren'Py 6 was released. Compared to that release, Ren'Py
7 adds many features uses have long since come to consider core parts of
the engine, such as ATL, Screen Language, OpenGL acceleration, support for
the Android and iOS platforms, Translations, Accessibility, and so much more.

Thanks to everyone who created with Ren'Py during the Ren'Py 6 series, when
Ren'Py and visual novels went from a tiny niche to something that is popular
and culturally relevant. I look forward to seeing where Ren'Py 7 takes us.

Compared to Ren'Py 6.99.14.3, this release adds a new layered image system,
which provides a cleaner replacement for the use of LiveComposite and
ConditionSwitch when it comes to building sprites from layered images
created in paint programs. There is a new syntax for such images, and
portions can be defined automatically. Layered images also interact better
with other portions of Ren'Py, such as the image predictor and interactive
director.

Other major changes are:

* The ability to apply transitions to specific layers, making it possible to
  dissolve in a sprite while text is being shown.
* A second row of ruby or interlinear text can now be shown.
* A way of converting strings into custom displayables.
* A French translation of the launcher and The Question.
* An editing pass over the reference manual.

Apart from these, this release includes a few fixes and minor new features.
As always, check the changelog for complete details.

Ren'Py 7 is brought to you by
`over 100 people from around the world <https://www.renpy.org/doc/html/credits.html>`_,
and myself, Tom "PyTom" Rothamel.
""",
    history="""\
""",

    full_html="""\
<img src="/static/7.0.0.jpg" alt="" style="width: 100%">
""",

    top_html="""\
""",
)
