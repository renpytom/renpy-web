#coding=utf-8
# This file contains data about Ren'Py, and its various
# releases. Think of it as a kind of database, except that it's stored
# as code rather than as data.

from model import *

# A list of releases. This is automatically filled up when we execute the
# Release and WikiRelease statement-commands, below.
releases = [ ]

# All aliases.
aliases = [ ]

# Private Prerelease checklist:
#
# 1. prerelease=True
# 2. invisible=True
# 3. version
# 4. patch=0
# 5. patch_date=None
# 6. name
# 7. sizes
# 8. -
# 9. announcement.

# Patch release checklist:
#
# 1. Bump patch.
# 2. Update patch_date.
# 3. Add to history.

# Final release checklist:
#
# 1. Bump date.
# 2. prerelease=False
#
# Remember to add.py --release !

# To get the list of contributors to a release, we can use the command:
# git shortlog 7.0..HEAD


Release(
    prerelease=True,
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
""".decode("utf-8"),
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
""".decode("utf-8"),
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
""".decode("utf-8"),
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
""".decode("utf-8"),
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
""".decode("utf-8"),
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
""".decode("utf-8"),
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
""".decode("utf-8"),
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
""".decode("utf-8"),
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
""".decode("utf-8"),
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
""".decode("utf-8"),
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
""".decode("utf-8"),
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
""".decode("utf-8"),
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
    version="6.99.14.3",
    pygame="-2.1.0",
    date="April 5, 2018",
    patch=None,
    name="A funny thing happened.",
    world_order=9,
    announcement="""\
I've released Ren'Py 6.99.14.3, which fixes a few regressions introduced in
6.99.14.2, most notably one in screens that could cause problems by failing
to propagate data through screen updates. (This could cause transforms to
repeat, as well as other strange problems. It only manifested for displayables
directly or indirectly inside for loops.)

It also fixes several other issues, and makes the AlphaMask displayable
more useful.

Please see the `6.99.14 release notes <https://www.renpy.org/release/6.99.14>`_,
`6.99.14.1 release notes <https://www.renpy.org/release/6.99.14.1>`_,
and `6.99.14.2 release notes <https://www.renpy.org/release/6.99.14.2>`_ for
what's new in these releases.

Ren'Py 6.99.14 is brought to you by:

* Andy_kl
* Eevee (Lexy Munroe)
* Eliza Velasquez
* El-Unicorn
* Enerccio
* Kevin Turner
* Maxwell Paul Brickner
* Peter Vanusanik
* Ria-kon
* Nyyatrap
* Vollschauer
* William Tumeo
* Xavi-mat

and myself, Tom "PyTom" Rothamel.
""".decode("utf-8"),
    history="""\
""",

    full_html="""\
<img src="/static/6.99.14.jpg" alt="" style="width: 100%">
""",

    top_html="""\
""",
)


Release(
    prerelease=False,
    invisible=False,
    version="6.99.14.2",
    pygame="-2.1.0",
    date="March 27, 2018",
    patch=None,
    name="A funny thing happened.",
    world_order=9,
    announcement="""\
I've released Ren'Py 6.99.14.2, a release that adds support for the Atom
text editor to Ren'Py. Atom is a modern and approachable editor with
support for a number of features, like code folding.

To try Atom, please go to the Ren'Py preferences, and select Atom as
your text editor. The normal Ren'Py text editing features will then
use Atom. Further customization can be done inside Atom itself, including
switching between dark and light themes.

This release also includes a few new features, and a number of important fixes,
so everyone should upgrade.

Special thanks to William Tumeo for the initial creation of the language-renpy
Atom plugin, and then for transferring it to the Ren'Py project.

Please see the `6.99.14 release notes <https://www.renpy.org/release/6.99.14>`_
and `6.99.14.1 release notes <https://www.renpy.org/release/6.99.14.1>`_ for
what's new in these releases.

Ren'Py 6.99.14 is brought to you by:

* Andy_kl
* Eevee (Lexy Munroe)
* Eliza Velasquez
* Enerccio
* Kevin Turner
* Maxwell Paul Brickner
* Peter Vanusanik
* Ria-kon
* Nyyatrap
* Vollschauer
* William Tumeo
* Xavi-mat

and myself, Tom "PyTom" Rothamel.
""".decode("utf-8"),
    history="""\
""",

    full_html="""\
<img src="/static/6.99.14.jpg" alt="" style="width: 100%">
""",

    top_html="""\
""",
)


Release(
    prerelease=False,
    invisible=False,
    version="6.99.14.1",
    pygame="-2.1.0",
    date="February 4, 2018",
    patch=None,
    name="A funny thing happened.",
    world_order=8,
    announcement="""\
I've released Ren'Py 6.99.14.1, a release focused on improving Ren'Py
performance (both perceived and actual) by improving image prediction.
This is done in a number of ways, such as reducing unnecessary locking,
reducing memory usage by reducing duplication and only storing
non-transparent portions of the image in memory, increasing the amount
of memory used for by the image cache, and more.

This release returns the framerate behavior to that in 6.99.13 and
earlier, where Ren'Py will slow down how quickly it updates the screen
when nothing changes. It also includes other improvements and fixes.

Please see the `6.99.14 release notes <https://www.renpy.org/release/6.99.14>`_
for what's new in that recent release.


Ren'Py 6.99.14 is brought to you by:

* Eliza Velasquez
* Enerccio
* Peter Vanusanik
* Ria-kon
* Nyyatrap
* Vollschauer
* Xavi-mat

and myself, Tom "PyTom" Rothamel.

This release is dedicated to the memory of `SusanTheCat <https://lemmasoft.renai.us/forums/memberlist.php?mode=viewprofile&u=7524>`_.
""".decode("utf-8"),
    history="""\
""",

    full_html="""\
<img src="/static/6.99.13.jpg" alt="" style="width: 100%">
""",

    top_html="""\
""",
)


# To get the list of contributors to a release, we can use the command:
# git shortlog 6.99..HEAD
Release(
    prerelease=False,
    invisible=False,
    version="6.99.14",
    pygame="-2.1.0",
    date="January 14, 2018",
    patch=None,
    name="A funny thing happened.",
    world_order=8,
    announcement="""\
So, remember how 6.99.13 was supposed to be the last release before
Ren'Py 7? Well, a funny thing happened - after a very productive month
or two, we have Ren'Py 6.99.14 with many improvements.

As an important note, the first time you open a game in 6.99.14, it will
open much slower as Ren'Py compiles all the Python expressions it encounters.
The game will open faster the second and later times it is run, and will run
faster once it is open.

Some of the improvements are:

* The performance of Ren'Py has been improved in multiple ways, and the
  apparent responsiveness has been improved even more.
* A new multiple character dialogue system makes it possible for multiple
  characters to display dialogue on the screen at once.
* A new GUI preference system works with the new GUI to make it easier to
  create preferences that customize the look of the Ren'Py GUI.
* A new tooltip system makes it easier to write tooltips.
* Ren'Py now supports TLS on multiple platforms, making it possible to
  use HTTPS to connect to servers to transfer game data.

This release also fixes issues with movie playback and android apps displaying
a black screen, along with other improvements mentioned in the changelog.

Ren'Py 6.99.14 is brought to you by:

* Eliza Velasquez
* Maissara Moustafa
* Morgan Willcock
* Rastagong
* Ria-kon
* Nyaatrap
* Vollschauer

and myself, Tom "PyTom" Rothamel.
""".decode("utf-8"),
    history="""\
""",

    full_html="""\
<img src="/static/6.99.13.jpg" alt="" style="width: 100%">
""",

    top_html="""\
""",
)


# To get the list of contributors to a release, we can use the command:
# git shortlog 6.99..HEAD
Release(
    prerelease=False,
    invisible=False,
    version="6.99.13",
    pygame="-2.1.0",
    date="October 29, 2017",
    patch=None,
    name="We came in peace.",
    world_order=8,
    announcement="""\
I'm happy to announce Ren'Py 6.99.13, the last in a series of releases
that will culminate in Ren'Py 7. This release improves Ren'Py for creators
of all experience levels. Some of the highlights of this release are:

* The two games that are bundled with Ren'Py have both been remade. Both
  are now in the 16:9 aspect ratio and use modern Ren'Py programming
  techniques. The Tutorial has been rethought, and is now structured
  to be a basic and in-depth class in Ren'Py, with hundreds of new examples.
  (The old tutorial may still be used when a translation exists for a language.)
* Ren'Py now ships with the Interactive Director, which can be accessed by
  pressing 'D'. The Director allows one to edit scripts from inside Ren'Py,
  adding and modifying the scene, show, hide, with, play, queue, stop and
  voice statements.
* Ren'Py now runs on the Raspberry Pi. Raspberry Pi files can be downloaded
  and added to a Ren'Py release, though it's the creator's responsibility to ensure
  that their project runs in the limited memory available on that platform.
* Ren'Py now takes advantage of Non-Power of Two (NPOT) textures to reduce
  memory usage when supported on a platform. Memory usage can be reduced
  further by setting config.cache_surfaces to False.
* The functionality of the {a} text tag, which introduces a hyperlink, has
  been improved. It's now possible to use a hyperlink to jump to a label,
  call a label, or show a screen.
* The say statement has been extended to take arguments. This new syntax can
  be used by advanced creators to provide additional information to a say
  statement.
* Ren'Py now loads files in a second thread, preventing sound playback and
  looping from causing drops in the framerate.
* Translations of the launcher to French and Brazilian Portuguese have been added,
  while the new tutorial is also available in Russian.

In addition to these, dozens of minor improvements are mentioned in the
changelog.

Ren'Py 6.99.13 is brought to you by:

* Alexandre Tranchant
* Andrew Savchenko
* Gregory Pease
* Gustavo Carvalho
* Ian Leslie
* Kevin Turner
* Lore
* Maxwell Paul Brickner
* Morgan Willcock
* Mugenjohncel
* Pratomo Asta N
* Renoa
* Ria-kon
* Nyaatrap
* Vollschauer
* Xavi-mat
* Zedraxlo

and myself, Tom "PyTom" Rothamel.
""".decode("utf-8"),

    history="""\
""",

    full_html="""\
<img src="/static/6.99.13.jpg" alt="" style="width: 100%">
""",

    top_html="""\
""",
)

Release(
    prerelease=False,
    invisible=False,
    version="6.99.12",
    pygame="-2.1.0",
    date="December 20, 2016",
    patch="4",
    name="We get the job done.",
    world_order=7,
    announcement="""\
I'd like to announce Ren'Py 6.99.12, the latest in a series of releases
that will culminate in Ren'Py 7, and one of the biggest Ren'Py releases
to date.

This release focuses on improving support for new versions of macOS, by
changing the macOS-specific package to support code signing and work
correctly when path randomization is enabled. When run on macOS, Ren'Py
can automatically sign the application, and create a signed disk image.
The launcher can launch older Ren'Py applications on macOS Sierra, to
improve compatibility with older games.

Because of this change, the -all distribution has been retired, replaced
with -mac and a new -pc distribution that supports Windows and Linux.

The other main focus of this release is improving support for translation
of the new GUI. Translating Ren'Py now translates both the launcher and the
interface of new games created in the launcher language. It is also possible
to change the font used by the launcher and new projects. There is a page
about translating Ren'Py in the documentation, to guide the process.

In addition to these major focuses, this release includes a number of new
features and bug fixes.

Ren'Py 6.99.12 is brought to you by:

* Bryan Tsang
* Daniel Luque
* Gas
* Joshua Fehler
* Morgan Willcock
* Merumelu
* Nyaatrap
* Pratomo Asta Nugraha
* Project Gardares
* Renoa
* Ria-kon
* Spiky Caterpillar
* Vollschauer
* Xela
* Xavi-Mat

and myself, Tom "PyTom" Rothamel.
""".decode("utf-8"),

    history="""\
**6.99.12.4.2187**: February 28, 2017
    This release fixes a number of bugs, including one that would cause the
    renpy.input function to crash. It improves the console (accessed with
    shift+O), and updates translations.

**6.99.12.3.2123**: February 12, 2017
    This release fixes a number of bugs. It also adds and renames gui variables
    so that every text property can be controlled by a gui variable, and adds
    support for the new Ren'Py Interactive Director.

**6.99.12.2.2029**: December 31, 2016
    This fixes a bug that could prevent viewport children from becoming focused,
    and a bug that prevented the RAPT and Renios DLC from being downloaded
    properly. It also adds functionality to support the interactive director.

**6.99.12.1.2012**: December 23, 2016
    This fixes a major issue that could cause MultiPersistent data to not work
    on systems using non-ASCII character sets. It also fixes other bugs, and
    updates the Indonesian translation.
""",

    full_html="""\
<img src="/static/6.99.11.jpg" alt="" style="width: 100%">
""",

    top_html="""\
""",
)


Release(
    prerelease=False,
    invisible=False,
    version="6.99.11",
    pygame="-2.1.0",
    prerelease_date=None,
    date="September 5, 2016",
    patch=None,
    patch_date=None,
    name="Who tells your story?",
    exe=None,
    bz2=None,
    zip=None,
    powerpc=False,
    world_order=6,
    announcement="""\
I'd like to announce Ren'Py 6.99.11, the latest in a series of releases
that will culminate in Ren'Py 7, and one of the biggest Ren'Py releases
to date.

The biggest change is a new default GUI framework. Out of the box, the new
GUI looks more modern, works across a range of screen sizes, and supports
mobile devices out of the box. The GUI is also easier for creators of all
skill levels to customize, with re-theming accomplished by replacing image
files and optionally adjusting variables. The Ren'Py documentation now
includes a GUI customization guide explaining how to completely retheme
the new GUI.

Thanks go to Auro-Cyanide for the original design of the new GUI. (But
don't blame her - we've had to stray quite a bit from that design in pursuit
of resolution independence.)

There have been a number of features added to Ren'Py to support the new GUI.

* Ren'Py now natively supports a dialogue history/readback system.
* File pages can be renamed by clicking on the page title/number.
* Style properties that use image filenames can take a [prefix\_] substitution,
  which causes a style prefix search.

And the usual set of non-GUI-related changes:

* Android support has been partially rewritten. It now supports x86 in addition
  to ARM, supports immersive mode, and fixes problems downloading Android
  dependencies.
* Ren'Py supports Chrome OS by converting an Android package using the Android
  Runtime for Chrome tool.
* The Ren'Py script language supports locally-scoped labels.
* Transforms support tiling the child multiple times, and panning over the child
  image by an angle.

A Vietnamese translation of the launcher and tutorial has been added by Thuong
Nguyen Huu. An Indonesian translation of the launcher and default project has
been contributed by Pratomo Asta Nugraha.

Ren'Py 6.99.11 is brought to you by:

* Caryoscelus
* Diapolo10
* Edward Betts
* Ferdinand Thiessen
* Kevin Turner
* Morgan Willcock
* Nolanlemahn
* Pratomo Asta N
* Sapphi
* Shiz
* Vollschauer
* Xavi-mat
* Xela

and myself, Tom "PyTom" Rothamel.
""".decode("utf-8"),

    history="""\
The history of older Ren'Py 6.99 releases can be found at the following
URLs:

* https://www.renpy.org/release/6.99.10
* https://www.renpy.org/release/6.99.9
* https://www.renpy.org/release/6.99.8
* https://www.renpy.org/release/6.99.7
* https://www.renpy.org/release/6.99.6
* https://www.renpy.org/release/6.99.5
* https://www.renpy.org/release/6.99
""",

    full_html="""\
<img src="/static/6.99.11.jpg" alt="" style="width: 100%">
""",

    top_html="""\
""",
    )


Release(
    prerelease=False,
    invisible=False,
    version="6.99.10",
    pygame="-2.1.0",
    prerelease_date="March 21, 2016",
    date="March 24, 2016",
    patch=None,
    patch_date=None,
    name="NaNoRenO - The Other March Madness",
    exe=36,
    bz2=54,
    zip=59,
    powerpc=False,
    world_order=6,
    announcement="""\
I'd like to announce Ren'Py 6.99.10, the latest in a series of releases that
will culminate in Ren'Py 7. This release fixes two regressions that were
introduced in Ren'Py 6.99.9:

* Ren'Py would fail to start if a DirectInput gamepad could not be opened in
  exclusive mode.
* Ren'Py would fail to start with an SDL error on certain Android devices.

This release also includes:

* A new vpgrid widget, which combines a viewport and a grid into a single
  widget, with optimized rendering.
* InputValues that can be with the text input widget to allow multiple text
  inputs to be displayed at once.
* A Greek translation of the launcher, contributed by George Economidis.

Ren'Py 6.99.10 is brought to you by:

* George Economidis
* Jackmcbarn

and myself, Tom "PyTom" Rothamel.
""".decode("utf-8"),

    history="""\
The history of older Ren'Py 6.99 releases can be found at the following
URLs:

* https://www.renpy.org/release/6.99.9
* https://www.renpy.org/release/6.99.8
* https://www.renpy.org/release/6.99.7
* https://www.renpy.org/release/6.99.6
* https://www.renpy.org/release/6.99.5
* https://www.renpy.org/release/6.99
""",

    full_html="""\
""",

    top_html="""\
""",
    )


Release(
    prerelease=False,
    invisible=False,
    version="6.99.9",
    pygame="-2.1.0",
    prerelease_date="February 28, 2016",
    date="March 07, 2016",
    patch=None,
    patch_date=None,
    name="To the nines.",
    exe=36,
    bz2=54,
    zip=59,
    powerpc=False,
    world_order=6,
    announcement="""\
I'm happy to announce Ren'Py 6.99.9, the latest in a series of releases that
will culminate in Ren'Py 7. This release features a full rewrite of the audio
and video playback code, which allows for a number of often-requested features:

* Partial playback of audio files, including the specification of start,
  end, and loop points.
* A new audio channel that allows the playback of multiple sound files at
  once, for use by interface and game sound
* The ability to play multiple movies at once, and to seamlessly loop
  movies.
* Movie-backed sprites that use a pair of movies, one for the color channel
  and one containing alpha (opacity) information.

This release includes a major bugfix involving fullscreen games on Windows
when DPI scaling is used, and a number of other fixes and new features.

Ren'Py 6.99.9 is brought to you by:

* Carl
* Markus Koschany
* Shiz
* Vollschauer

and myself, Tom "PyTom" Rothamel.
""".decode("utf-8"),

    history="""\
The history of older Ren'Py 6.99 releases can be found at the following
URLs:

* https://www.renpy.org/release/6.99.8
* https://www.renpy.org/release/6.99.7
* https://www.renpy.org/release/6.99.6
* https://www.renpy.org/release/6.99.5
* https://www.renpy.org/release/6.99
""",

    full_html="""\
""",

    top_html="""\
""",
    )


Release(
    prerelease=False,
    invisible=False,
    version="6.99.8",
    prerelease_date="December 12, 2015",
    date="December 25, 2015",
    patch=None,
    patch_date=None,
    name="Here's to the crazy ones.",
    exe=34,
    bz2=48,
    zip=52,
    powerpc=False,
    world_order=6,
    announcement="""\
I'm pleased to announce Ren'Py 6.99.8. This is the latest in a series of
releases that introduce the new features that will make up Ren'Py 7. Ren'Py
6.99.8 fixes a bug with text spacing introduced in 6.99.7, and also adds
new features, including:

* The ability to associate an image tag with a layer, transform, and zorder,
  and a new function that makes adding custom layers easier.
* A full set of easing functions that can be used with ATL.
* An overhaul of new-style side images, allowing transforms (and hence,
  transitions) to be applied when the side image changes.
* A new PushMove transition class, which uses the new scene to push the
  old one out.
* HighDPI display support has been added for the Windows platform.

As usual, other features have been added, bugs have been fixed, and Ren'Py
has been generally improved.

Ren'Py 6.99.8 is brought to you by:

* BlackDragonHunt/Mangagamer
* Kalawore
* Kuroonehalf
* Nyaatrap
* Rikxz
* Vollschauer

and myself, Tom "PyTom" Rothamel.
""".decode("utf-8"),

    history="""\
The history of older Ren'Py 6.99 releases can be found at the following
URLs:

* http://www.renpy.org/release/6.99.7
* http://www.renpy.org/release/6.99.6
* http://www.renpy.org/release/6.99.5
* http://www.renpy.org/release/6.99
""",

    full_html="""\
<img src="/static/6.99.7.jpg" title="Syrup and the Ultimate Sweet, running under Ren'Py 6.99.7." style="width: 100%">
""",

    top_html="""\
""",
    )


Release(
    prerelease=False,
    invisible=False,
    version="6.99.7",
    prerelease_date="October 25, 2015",
    date="November 1, 2015",
    patch=None,
    patch_date=None,
    name="Here's to the crazy ones.",
    exe=34,
    bz2=48,
    zip=52,
    powerpc=False,
    world_order=6,
    announcement="""\
I'm pleased to announce Ren'Py 6.99.7. This is the latest in a series of
releases that introduce the new features that will make up Ren'Py 7. Ren'Py
6.99.7 is primarily to fixing bugs and rendering issues introduced in 6.99.7,
but also introduces a number of new features, including:

* A new dynamic images feature that lets Ren'Py interpolate text into displayables
  at the start of each interaction. This should make certain common patterns much
  easier to implement, such as dressup code that previously required a large
  number of ConditionSwitches.
* An extension to the define statement that makes it possible to define config
  and persistent variables. Persistent variables use special semantics to ensure
  a persistent variable is only defined once.

A number of other smaller features have been added, as described in the changelog.
Over a dozen fixes to bugs and regressions are listed in the changelog, and
there are probably a few more fixes that didn't make it.

Ren'Py 6.99.7 is brought to you by:

* Diapolo10
* Emmeken
* Kalawore
* Javimat
* Pavel Langwell
* Ricardo Pérez
* Spiky Caterpillar

and myself, Tom "PyTom" Rothamel.
""".decode("utf-8"),

    history="""\
The history of older Ren'Py 6.99 releases can be found at the following
URLs:

* http://www.renpy.org/release/6.99.6
* http://www.renpy.org/release/6.99.5
* http://www.renpy.org/release/6.99
""",

    full_html="""\
<img src="/static/6.99.7.jpg" title="Syrup and the Ultimate Sweet, running under Ren'Py 6.99.7." style="width: 100%">
""",

    top_html="""\
""",
    )


Release(
    prerelease=False,
    invisible=False,
    version="6.99.6",
    prerelease_date="September 14, 2015",
    date="September 14, 2015",
    patch=None,
    patch_date=None,
    name="Here's to the crazy ones.",
    exe=34,
    bz2=48,
    zip=52,
    powerpc=False,
    world_order=6,
    announcement="""\
I'm pleased to announce Ren'Py 6.99.6. This is the latest in a series of
releases that introduce the new features that will make up Ren'Py 7.

The 6.99.6 release:

* Has much better support for high-resolution displays. Retina displays are now supported
  on Mac OS X and iOS - the latter support was broken by 6.99.5. On all platforms,
  Ren'Py will try to render text at the display resolution, rather than the game's
  resolution. This means that text should remain sharp even as the window is scaled up.

* Joystick support has been removed from Ren'Py, and replaced with gamepad
  support based on SDL2's new controller API. This API maps all sorts of gamepads
  to an Xbox-style controller, making standard bindings possible in the same way
  such bindings are possible for a keyboard and mouse.

* Ren'Py now automatically backs up .rpy files when a game changes. These script
  files are backed up to the system-wide save directory.

This release also includes a number of other fixes and improvements.

We'd like to thank Patrick Dawson for writing much of the code of Pygame_SDL2,
a new, SDL2-based implementation of the Pygame API, and Chris Mear, who created
the initial iOS port of Ren'Py that our current support is based on. Other
contributors include:

* Asfdfdfd
* Baekansi
* Bbs3223474
* Beuc
* Caryoscelus
* Daniel Luque
* Denzil
* Diapolo10
* Evilantishad0w
* Giuseppe Bertone
* Huang Junjie
* Javimat
* Konstantin Nikolayev
* Kyouryuukunn
* Lapalissiano
* Nolanlemahn
* Renoa
* RangHo Lee
* rivvil
* Tlm-2501
* Zigmut

and myself, Tom "PyTom" Rothamel.
""",

    history="""\
The history of older Ren'Py 6.99 releases can be found at

  http://www.renpy.org/release/6.99.5

and

  http://www.renpy.org/release/6.99
""",

    full_html="""\
<img src="/static/6.99.jpg" alt="Screenshot of Ren'Py 6.17" style="width: 100%">
""",

    top_html="""\
""",
    )

Release(
    prerelease=False,
    invisible=False,
    version="6.99.5",
    prerelease_date="July 16, 2015",
    date="July 19, 2015",
    patch=None,
    patch_date=None,
    name="Here's to the crazy ones.",
    exe=34,
    bz2=48,
    zip=52,
    powerpc=False,
    world_order=6,
    announcement="""\
I'm pleased to announce Ren'Py 6.99.5. This is the latest in a series of
releases that introduce the new features that will make up Ren'Py 7.

The 6.99.5 release focuses on mobile platforms. It massively improved
startup time, which helps all platforms, but is especially important
on the slower mobile devices. It also improves support for iOS 8, and
has other fixes an improvements.

We'd like to thank Patrick Dawson for writing much of the code of Pygame_SDL2,
a new, SDL2-based implementation of the Pygame API, and Chris Mear, who created
the initial iOS port of Ren'Py that our current support is based on. Other
contributors include:

* Asfdfdfd
* Baekansi
* Bbs3223474
* Beuc
* Caryoscelus
* Daniel Luque
* Denzil
* Diapolo10
* Evilantishad0w
* Giuseppe Bertone
* Huang Junjie
* Javimat
* Konstantin Nikolayev
* Kyouryuukunn
* Lapalissiano
* Nolanlemahn
* Renoa
* RangHo Lee
* rivvil
* Tlm-2501
* Zigmut

and myself, Tom "PyTom" Rothamel.
""",

    history="""\
The history of older Ren'Py 6.99 releases can be found at

  http://www.renpy.org/release/6.99
""",

    full_html="""\
<img src="/static/6.99.jpg" alt="Screenshot of Ren'Py 6.17" style="width: 100%">
""",

    top_html="""\
""",
    )


Release(
    prerelease=False,
    invisible=False,
    version="6.99",
    prerelease_date="March 19, 2015",
    date="March 25, 2015",
    patch=4,
    patch_date="May 27, 2015",
    name="Here's to the crazy ones.",
    exe=34,
    bz2=48,
    zip=52,
    powerpc=False,
    world_order=6,
    announcement="""\
I'm pleased to announce Ren'Py 6.99 "Here's to the crazy ones." This release
focuses on modernizing Ren'Py by moving to the SDL2 family of libraries. This
modernization will lead to a series of benefits, both now and in the future.

This release is being managed as a rolling release leading to Ren'Py 7.0.
New features may be added in point releases.

Perhaps the most obvious benefit is the addition of iOS support. Ren'Py can
now produce iOS apps, targeting iPhone and iOS devices. To develop for iOS,
you will need a Macintosh computer and paid iOS developer license, and will
need to customize the interface to conform to iOS policies.

In addition, this release includes:

* Rewritten Android support, based on SDL2. Among other things, Android now
  supports the onscreen keyboard, rotating the screen, and bidirectional text.
* Audio playback, using the same code on desktop and mobile platforms, so the
  same audio files can be used on all platforms Ren'Py supports.
* Support for Input Methods (IMEs), allowing text entry in non-English languages.
* A high-level achievement API, including support for Steam achievements. (Steam
  support will be made available on request to Steam developers.)
* Improved support for custom text tags.
* A Russian translation of the tutorial game, and a Finnish translation of
  the launcher.

To this, the 6.99.2 release adds:

* Support for the images directory. Image files placed into this directory
  are automatically defined as images in Ren'Py,
* The new AlphaMask displayable, which allows the alpha channel of one
  displayable to be masked by that of another.

The 6.99.4 release adds:

* The new default statement, which is used to set the initial value of a
  variable in a game.
* Support for the transclusion of screen language code inside use statements,
  and support for creator-defined screen language statements.

The 6.99.5 release adds:

* Much faster startup, especially on mobile platforms.
* Better support for iOS 8.
* Many other small features.

These releases also include a number of other fixes and improvements.

We'd like to thank Patrick Dawson for writing much of the code of Pygame_SDL2,
a new, SDL2-based implementation of the Pygame API, and Chris Mear, who created
the initial iOS port of Ren'Py that our current support is based on. Other
contributors include:

* Asfdfdfd
* Baekansi
* Bbs3223474
* Beuc
* Caryoscelus
* Daniel Luque
* Denzil
* Diapolo10
* Evilantishad0w
* Giuseppe Bertone
* Huang Junjie
* Javimat
* Konstantin Nikolayev
* Kyouryuukunn
* Lapalissiano
* Nolanlemahn
* Renoa
* RangHo Lee
* rivvil
* Tlm-2501
* Zigmut

and myself, Tom "PyTom" Rothamel.
""",

    history="""\
**6.99.5.602**: July 19, 2015
    This release improves startup time, improves iOS 8 support, and
    includes other improvements and fixes.

**6.99.4.467**: May 27, 2015
    This release adds new features. It also fixes a number of bugs and
    performance problems.

**6.99.3.404**: April 26, 2015
    This removes extraneous code that was causing problems.

**6.99.2.403**: April 25, 2015
    This release adds new features, including the images directory and the
    AlphaMask displayable. It also fixes bugs.

**6.99.1.329**: March 29, 2015
    This release fixes crashes that occurred in a number of important cases,
    including non-ASCII directory names on Windows systems, 16-bit display
    depths, and display rotation when targeting recent versions of Android.

    It also fixes several non-crash bugs, adds three new functions, and
    updates the Spanish and Japanese translations.
""",

    full_html="""\
<img src="/static/6.99.jpg" alt="Screenshot of Ren'Py 6.17" style="width: 100%">
""",

    top_html="""\
""",
    )


Release(
    prerelease=False,
    invisible=False,
    version="6.18",
    prerelease_date="August 24, 2014",
    date="September 12, 2014",
    patch=3,
    patch_date="October 21, 2014",
    name="... through shared popular culture.",
    exe=31,
    bz2=44,
    zip=48,
    android=True,
    powerpc=False,
    deps="6.17.0",
    world_order=5,
    announcement="""\
I'm pleased to announce Ren'Py 6.18 "... through shared popular culture.". Major
improvements in this release include:

* A full rewrite of screen language that has the potential for significantly
  improved performance.
* Self-voicing support that provides a level of accessibility to blind
  users.
* A high-level Android in-app purchasing framework.
* New Italian, Portuguese, Simplified Chinese, and Traditional Chinese
  translations, and a new German template.

This release also includes many other features and fixes. It has been brought
to you by:

* Koichi Akabe
* Civalin
* Duanemoody
* Helloise
* Huanxuantian
* Daniel Luque
* Javimat
* Kyouryuukunn
* Emmannuel Marty
* Mrstalker
* Mugenjohncel
* Nojoker
* Oshi-Shinobu
* Renoa
* Tom "PyTom" Rothamel
* Shiz
* Winter Wolves
""",

    history="""\
**6.18.3.761**:
    This release improves prediction, adds the new screen language "showif"
    statement, adds minor features, and fixes bugs.

**6.18.2.729**:
    This release adds many small new features, and fixes several minor bugs.
    It also adds the Traditional Chinese translation.

**6.18.1.670**: September 22, 2014
    This release fixes a number of bugs in Ren'Py 6.18. It changes ATL behavior
    so that an ATL transform that is part of a screen will begin executing when
    the transform (rather than the screen) is first shown. It also adds a new
    placeholder image system, and a way to speak descriptive text as part of
    the self-voicing process.
""",

    full_html="""\
""",

    top_html="""\
""",
    )


Release(
    prerelease=False,
    invisible=False,
    version="6.17",
    prerelease_date="February 15, 2014",
    date="February 20, 2014",
    patch=7,
    patch_date="July 6, 2014",
    name="In This Decade...",
    exe=28,
    bz2=36,
    zip=39,
    android=True,
    powerpc=False,
    deps="6.17.0",
    world_order=5,
    announcement="""\
As we reach the tenth anniversary of the start of Ren'Py development,
I'm pleased to announce Ren'Py 6.17 "In This Decade...". Major improvements
in this release include:

* A rewrite of the Style system that should improve Ren'Py's performance.
* A new style statement that makes it easier to define styles.
* A rewritten shift+I style inspector lets you view those styles.
* A new "show layer" statement that makes it convenient to apply transforms
  and ATL transforms to entire layers at once.
* A new "window auto" statement that enables automatic management of the
  dialogue window.
* Several other syntax improvements.
* French and Russian translations.
* The integration of RAPT (the Ren'Py Android Packaging Tool) with the
  Ren'Py SDK. Ren'Py now downloads RAPT using the Ren'Py updater - it's
  no longer necessary to download RAPT separately.

This release also includes several other new functions and actions, and
major bugfixes that affect the Android platform.

This release has been brought to you by:

* Koichi "vbkaisetsu" Akabe
* CensoredUsername (C)
* kyouryuukunn
* Daniel Luque
* Renoa
* Tom "PyTom" Rothamel
* tlm-2501
""",

    history="""\
**6.17.7.521**: July 6, 2014
    This release updates the Android SDK to a working version, adds a low-level
    in-app purchasing framework, and fixes an issue with movie playback on
    desktop platforms.

**6.17.6.512**: May 7, 2014
    This release adds new German and Korean translations, and works around
    a bug that prevented the Ren'Py launcher from starting on certain macs.

**6.17.5.492**: May 1, 2014
    This release adds a new Arabic translation, and updates the Japanese and
    Spanish translations. It also fixes several bugs affecting the shift+R
    reload functionality, and provides several new features.

**6.17.4.409**: April 16, 2014
    This release fixes problems with Android (especially ones caused by a missing
    play licensing library), adds support for the Amazon Fire TV console, allows imagemaps
    in viewports, and prevents large memory leaks from occurring when shift+R is pressed.

**6.17.3.327**: March 4, 2014
    This release fixes a bug where Ren'Py would misparse properties and
    attributes that began with a Python operator. (For example, ``insensitive``,
    which begins with ``in``.) It also rewrites the missing image code to use
    styles and screens.

**6.17.2.319**: February 28, 2014
    This release adds a new "translate <i>language</i> style <i>style_name</i>"
    statement, which is used to customize styles in a particular language. It
    also improves scanning the projects directory and fixes various other
    issues.

**6.17.1.309**: February 24, 2014
    This release fixes a problem where an update could overwrite a file in
    the RAPT directory, preventing builds. It also updates and improves
    translations, and deals gracefully with improperly encoded files in
    the projects directory.
""",

    full_html="""\
<img src="/static/6.17.jpg" alt="Screenshot of Ren'Py 6.17">
""",

    top_html="""\
""",
    )


Release(
    prerelease=False,
    invisible=False,
    version="6.16",
    prerelease_date="November 4, 2013",
    date="November 6, 2013",
    patch=5,
    patch_date="December 17, 2013",
    name="In the Arena",
    exe=24,
    bz2=31,
    zip=34,
    android=True,
    powerpc=False,
    deps="6.15.5",
    world_order=4,
    announcement="""\
On behalf of the Ren'Py team, I'm pleased to announce Ren'Py 6.16 "In the
Arena". This release brings with it:

* Improved Android support, including the ability to build APKs from the
  launcher, support for Expansion APKs, and support for televison-based
  consoles like the OUYA.
* The ability to associate JSON information with a save file, and access
  that information in the load and save screens.
* Save file synchronization when Ren'Py is run from a shared directory.
* Support for a creator dumping the text of the game script, and for
  automatically playing appropriately-named voice files.
* Improvements to the gallery (including a new navigation overlay) and the
  music room (such as shuffle, loop, and single-track toggles.)
* A Japanese translation of the launcher, template, and documentation.

As well as a number of minor improvements and bugfixes.

This release has been brought to you by:

* javimat
* kyouryuukunn
* Koichi "vbkaisetsu" Akabe
* Daniel Luque
* Tom "PyTom" Rothamel

With thanks to antoinentx for improving support for international
directories, and everyone who contributed ideas, bug reports, and feedback
to Ren'Py development.
""",

    history="""\
**6.16.5.525**: December 17, 2013
    This release adds back a missing file that is required to launch jEdit.

**6.16.4.524**: December 16, 2013
    This release fixed Android building support, the Replay function, and
    the scanning of save games. It also includes a number of improvements
    to the documentation.

**6.16.3.502**: November 29, 2013
    This release fixes a problem that could cause excessive texture memory
    usage. It also improves Android support in several ways, making it
    possible for Ren'Py games to appear in the tablet section of Google Play.

**6.16.2.490**: November 21, 2013
    This release adds new Spanish translations of the launcher and template
    game. It adds a new function that gets the mouse position, and fixes
    bugs, typos, and usability flaws in the launcher and Ren'Py proper.

**6.16.1.409**: November 9, 2013
    This release includes a number of bug fixes related to translation and
    running in non-ASCII directories, including a fix to the updater. It
    also includes documentation improvements.
""",

    full_html="""\
<img src="/static/6.16.jpg" width="1000" alt="Screenshot of Ren'Py 6.16">
""",

    top_html="""\
""",
    )


Release(
    prerelease=False,
    invisible=False,
    version="6.15",
    prerelease_date="February 17, 2013",
    date="March 3, 2013",
    patch=7,
    patch_date="June 26, 2013",
    name="Foreign Policy",
    exe=22,
    bz2=27,
    zip=29,
    android=True,
    powerpc=False,
    deps="6.15.5",
    world_order=4,
    announcement="""\
I'm pleased to announce Ren'Py 6.15 "Foreign Policy", the result of about
six months of Ren'Py development. The main focus of this release was on
internationalization, the creation of a comprehensive translation system,
and better support for displaying Japanese text. Other new features
include:

* An interactive console that allows you to type Ren'Py and python commands,
  that can be accessed by typing shift+O.
* Screens now take positional and named parameters.
* Support for creating a replay gallery.
* Voice improvements, including the ability to mute particular voices.
* Support for skinning the launcher.

Ren'Py now includes a Japanese translation of the tutorial game, which can
be accessed from the preferences menu. For a full list of features and bug fixes,
please see the changelog.

Ren'Py 6.15 has increased the minimum requirements to run on the Macintosh
platform. It now requires a 64-bit Intel Macintosh running OS X 10.6 or
later.

Once again, this release has seen many contributions from the community. We
thank:

* Koichi Akabe for much of the new Japanese support and the Japanese
  translation of the tutorial game.
* Shiz, C, and Delta for the interactive Console.
* Ren for advice on how the translation system should work.

And, of course, everyone who contributed ideas, bug reports, and feedback
to Ren'Py development.
""",

    history="""\
**6.15.7.374**: June 26, 2013

    Fix a regression in ImageDissolve.

**6.15.6.372**: June 25, 2013

    This release includes improvements for the Android platform:

    * Assets are now read exclusively from the APK and expansion file.
    * Logs and tracebacks are placed on external storage.
    * Saves are placed on external storage, except when saves from
      older versions of Ren'Py exist.

    The GL2 shaders Ren'Py uses have been simplified in the (usual) case
    where no clipping is occurring. This leads to a noticeable speed
    improvement on Android, and potentially other platforms as well.

    An issue with Drag-and-drop has been fixed. Thanks go to Kinsman
    for contributing this fix.

    The Skip action now triggers the skip indicator. It also
    supports a new fast parameter, which causes skipping to the
    next menu.

    This release includes various minor changes to improve compatibility
    with very old Ren'Py games. (It now runs the Ren'Py 5 demo.)

**6.15.5.354**: June 6, 2013

    New features:

    * Additive blending, but only in the GL and DirectX/ANGLE renderers.
    * The new Flatten displayable, which combines multiple textures into one.

    Bug/Build fixes:

    * Before this release, Ren'Py produced zip files with unix modes that
      were writable by all users. If unzipped by a program that ignored the
      umask (like info-zip), the files could be overwritten by other users,
      causing a security problem.

      This problem only existed on unix-like systems that are shared by
      multiple users.
    * Ren'Py once again uses freetype auto-hinting when displaying fonts.
    * Ren'Py builds with the current libav (and ffmpeg).


**6.15.4.320**: April 6, 2013

    Bug fixes and improvements, including:

    * The 64-bit Linux version of Ren'Py is linked against the correct
      libraries. Versions 6.14.x and 6.15.0-3 were linked against
      incorrect Python libraries.

    * In the common case, the python interpreter is no longer locked while
      images are preloading. This helps prevent image preloading from causing
      framerate problems.

    * The new build.exclude_empty_directories variable determines if empty
      directories are included in archive files. Previously, this was
      undefined, and varied from platform to platform.


**6.15.3.303**: March 30, 2013

    Many bug fixes and improvements:

    * Image prediction has been broken up, such that a small amount of image
      prediction will run each frame. This prevent looping ATL animations
      from blocking image prediction.

    * When playing a fullscreen video, the screen will not be updated before
      the first frame is ready. This makes it possible to smoothly transition
      into a movie without displaying a black screen.

    * Fix problems with text input display on fonts that do not contain a
      zero-width space glyph.

    * Rare segfaults relating to font unloading have been fixed.

    * Fixed a memory leaks related to the rollback log and text layout cache.

    * Script parsing will fail with an error if a logical line exceeds 64 KB.

    * Quicksave will not fail of if the current file page is the auto-save page.

    * When a viewport changes size before being shown to the user, the offsets
      are re-applied to the viewport

    * SpriteManager now respects sprite zorder.

**6.15.2.280**: March 5, 2013

    This release fixes an issue with selecting the project directory on the
    mac. It also adds the ability to loop a single track in the music room.

**6.15.1.275**: March 5, 2013

    This release fixes the packaging of the editra text editor.
""",

    full_html="""\
<img src="/static/6.15.jpg" width="1000" height="367" alt="Screenshot of Ren'Py 6.15">
""",

    top_html="""\
""",
    )


Release(
    prerelease=False,
    invisible=False,
    version="6.14",
    prerelease_date="July 22, 2012",
    date="August 18, 2012",
    patch=1,
    patch_date="August 26, 2012",
    name="Steampunk Hamster",
    exe=22,
    bz2=27,
    zip=29,
    android=True,
    powerpc=True,
    deps="6.14.0",
    world_order=4,
    announcement="""\
I'm pleased to announce Ren'Py 6.14 "Steampunk Hamster", a release that brings
with it many improvements to Ren'Py and Ren'Py development.

Perhaps the largest theme of this release is that the tools we use to make
Ren'Py are now the same tools that we use to make Ren'Py games. Along this
vein:

* The Ren'Py launcher has been rewritten. It's now far more attractive, and
  contains a new script navigation function that makes it easy to navigate
  Ren'Py code.
* For most creators, we now recommend using the Editra editor with Ren'Py
  support. While still in beta, Editra is a lightweight and powerful
  programmer's editor to which we've added features that ease Ren'Py development.
  (jEdit is still supported, when Editra is not suitable.)
* The Ren'Py build process has also been updated. Now, it's possible to, in
  a single click, archive files and build a distribution of your game. Games
  may also use the same web updater that's used to update Ren'Py.

The engine proper has also seen many improvements:

* Video playback has been rewritten to improve robustness, performance, and
  stability. WebM is now a supported format.
* The new A White Tulip theme, written from scratch, provides some diversity
  to the look of Ren'Py games.
* Improvements to rollback, including the ability to fix rollback so that
  the user can't change a choice once made, without reloading.
* Several convenience shortcuts have been added to screens. A viewport with
  scrollbars can now be created as a single statement, and the style properties
  of text inside textbuttons and labels can be changed directly.
* An experimental new image load log helps creators understand image prediction
  and cache misses.
* Linux x86_64 is now supported by Ren'Py. Linux distributions will support
  both x86 and x86_64 cpus.
* Ren'Py ships with Python 2.7, and many of the libraries that underly
  Ren'Py have been updated.

This release has seen a huge amount of support from the community. I
especially thank:

* Edwin, for contributing the improved rollback support and several bug
  fixes and new features.
* Doomfest, for the visual design of the new launcher.
* Ren and Jake Staines for contributing the new A White Tulip theme.
* SleepKirby for improvements to Ren'Py's documentation.
* Apricotorange, for adding the NVL-mode tutorial to Ren'Py's documentation.

As of this release, Ren'Py uses github for project hosting.

Due to the change to the new web updater, shift+U updating from previous
versions of Ren'Py is not supported.
""",

    history="""\
**6.14.1.366**: August 26, 2012

   This release fixes a number of bugs in Ren'Py 6.14, including:

   * A major bug that prevented rollback and save from working for variables
     that are only updated in python functions.
   * Crashes during video and audio playback, especially on Mac OS X.
   * The version of zsync used by the updater didn't work on Windows XP.
   * Several string encoding problems in the new launcher.

   All users of Ren'Py 6.14.0 should upgrade to this release. Windows XP
   users should download the release again, while users of other supported
   operating systems can use the launcher to update.
""",

    full_html="""\
<img src="/static/t1000.jpg" width="1000" height="367" alt="Screenshot of Ren'Py, Editra, and the Ren'Py Launcher">
""",

    top_html="""\
""",
    )


Release(
    prerelease=False,
    invisible=False,
    version="6.13",
    date="September 14, 2011",
    patch=12,
    patch_date="April 17, 2012",
    name="Eye of the Storm",
    exe=21,
    zip=26,
    bz2=28,
    android=True,
    powerpc=True,
    deps="6.13.0",
    announcement="""\
Ren'Py 6.13 "Eye of the Storm" includes two fundamental improvements to Ren'Py. The
first is a complete rewrite of the text display code. In addition to supporting
new features such as interpolation of fields, kerning, ruby text, the new
display code is far faster than the previous code.

Ren'Py 6.13 also adds a DirectX rendering path. This new renderer should lead to
faster and more functional graphics display on Windows systems lacking OpenGL
support.

In addition to these major features, 6.13 adds a style preferences system, new
actions - including actions for image galleries and music rooms - and new
themes.

Some notes for upgraders:

* The change in interpolation may cause your old scripts to stop working. Please
  see the incompatible changes documentation for information on how to upgrade
  your script or enable a compatibility mode.

* The shift+U updater is not capable of upgrading 6.12.2 to this release. Please
  download 6.13 from the website.
""",

    history="""\
**6.13.12.1728**: April 17, 2012
    This release:

    * Fixes a related minimize and restore bug.
    * Improves compatibility with games that replace config.keymap.
    * Allows StylePreference and Language to work together.
    * Logs to the system temp directory if it can't writhe to the current
      directory.
    * Allows the screenshot filename to be configured by the creator.
    * Fixes keyboard adjustment of bars.
    * Updates the preferences screen when the window resizes.
    * Clears keyboard modifiers (like alt) when the window gains focus. This
      fixes a problem where the alt from an alt-tab would be remembered by
      Ren'Py, even after the key has been released.

**6.13.11.1715**: March 27, 2012
    This fixes a bug triggered (in some circumstances) by minimizing and
    restoring the game on Windows.

**6.13.10.1710**: March 25, 2012
    This release fixes a bug that can cause image buttons and image maps to
    not work on the software renderer. Other changes include more aggressive
    pruning of the rollback log to reduce memory consumption, improved handling
    of display initialization errors, and fixes to the loading of pure-python
    packages included as part of a game.

**6.13.9.1702**: March 14, 2012
    This release introduces the RAPT tool, a new way of packaging your Ren'Py
    game for use with Android. It fixes several bugs, including problems with
    hardware compatibility, non-ASCII filenames, and save file size.

    It introduces a new text editor documentation, backported from
    Ren'Py 6.14. If you use an editor other than jEdit, you'll need to
    check out the new text editor section of the Ren'Py documentation.


**6.13.8.1675**: January 17, 2012
    This release fixes a number of bugs and hardware compatibility problems in
    Ren'Py. It also includes improvements to new-style side image support, and
    adds the ability to run a callback after each Python block.

    It has one incompatible change - it reverts the removal of old-style
    substitution support. Please see the list of incompatible changes for
    more information.

**6.13.7.1646**: October 18, 2011
    Fixes a problem with substitutions in the launcher. Fixes a crash on font
    searching. On Android, merges multiple taps so as not to overwhelm the
    event queue.

**6.13.6.1642**: October 13, 2011
    Fixes a crash when loading automatically-created styles. Fixes a problem
    with quick saving not taking a screenshot. Fixes a problem with small solid
    textures not showing up, on the software renderer. Fixes a crash when
    playing back movies on Linux.

    This release introduces two new actions, QuickSave and QuickLoad, which
    are used for quick save and qick load functionality. If your game uses
    the new quick menu, please update it with the new code found in
    template/game/screens.rpy.

**6.13.5.1638**: October 10, 2011
    Fixes slow text.

**6.13.4.1637**: October 8, 2011
    Bugfix release 6.13.4 includes the following fixes:

    * Jumps from called screens now work. This fixes the developer menu.
    * Hitting shift+G in-game brings the user to the renderer selection menu.
    * Include all source required to rebuild Ren'Py.
    * Fix the renpy-ppc packaging.

**6.13.2.1632**: October 5, 2011
    Released bugfix release 6.13.2, which allows Text displayables to be
    instantiated in init blocks, and fixes error handling.

**6.13.1.1629**: October 3, 2011
    Released bugfix release 6.13.1, which makes Ren'Py run stably.

**6.13.0.1601**: September 14, 2011
    Official release.

**6.13.0.1601**: September 11, 2011
    Support reading files out of an Android package. User-defined statements can
    take blocks. A fix to lint with non-ASCII characters. A fix to error
    handling.

**6.13.0.1598**: September 5, 2011
    Adds error reporting when a non-string is used as text, fixes sound problems
    by moving to libav, and various other fixes.

**6.13.0.1594**: September 4, 2011
    First public pre-release.
""",

    aside_html="""\
""",
    ################################################################################
    #    top_html="""\
    # <div style="color: #800; background: #fcc; border: 2px solid #800; padding: 1em; margin: .5em; text-align: center;">
    # Ren'Py 6.13 has been reported to be incompatible with many users's systems.<br>
    # Please download and use <a href="/release/6.12.2">6.12.2</a> until we can fix these problems.
    # </div>
    # """
    ################################################################################
    )

Release(
    prerelease=False,
    invisible=False,
    version="6.12.2",
    name="Human Factor II",
    date="July 30, 2011",
    exe=21,
    zip=27,
    bz2=25,
    android=True,
    deps="6.11.0",
    announcement="""\
Ren'Py 6.12.2 "Human Factor II" is an update that fixes several bugs
found in Ren'Py 6.12.1.
""",

    history="""\
**6.12.2.1531**: July 30, 2011
    Initial release.
""",

    aside_html="""\
        <object width="380" height="238">
            <param name="movie" value="http://www.youtube.com/v/_MRDp2RHGEc?fs=1&amp;hl=en_US&amp;rel=0"></param>
            <param name="allowFullScreen" value="true"></param>
            <param name="allowscriptaccess" value="always"></param>
            <embed src="http://www.youtube.com/v/_MRDp2RHGEc?fs=1&amp;hl=en_US&amp;rel=0" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="380" height="238"></embed>
        </object>

    <i><a href="http://sonia-leong.livejournal.com/200681.html">Let Me Save You! Your Faithful Companion</a></i> time-lapse creation screencast. Courtesy Sonia Leong.
"""
    )


Release(
    prerelease=False,
    invisible=False,
    version="6.12.1",
    name="Human Factor",
    date="May 02, 2011",
    bugfix_revision=1520,
    bugfix_date="June 23, 2011",
    exe=21,
    zip=27,
    bz2=25,
    android=True,
    deps="6.11.0",
    announcement="""\
Ren'Py 6.12.1 "Human Factor" is the first of a series of minor releases
focusing on improving the experience of visual novel makers. This release
features several improvements to the process of showing images:

* Image attributes make it no longer necessary to specify every part
  of a changed image.
* The say statement can change image attributes when a character speaks.
* Side images can be specified with the image statement, and can be used
  with NVL-mode dialogue.
* Sticky transforms allow a transform to continue through an image change.

As these new features can change the behavior of existing games, it may be
convenient to disable them for in-development projects. Please see the list of
incompatible changes for instructions on how to do this.

The other major improvement is in error handling. Where previous versions of
Ren'Py would terminate on errors, 6.12.1 will display a screen that allows the
maker to edit problematic files and reload the game, and the user to rollback or
ignore the problem.

Ren'Py 6.12.1 also includes many other minor features and bug fixes, please
see the full changelog for more details.
""",

    history="""\
**6.12.1.1520**: June 23, 2011
    A major bugfix release, including:

    * Fixed a problem with texture upload that made games noticeably slower.
    * A better default size for windows on small monitors, like netbooks.
    * xfill and yfill now work for vbox and hbox, respectively.
    * Click-to-continue fixes.
    * Side image fixes.

**6.12.1.1502**: May 16, 2011
    Compatibility fixes for Android. This release only consisted of
    new versions of Ren'Py for Android and renpy-apk. If you're only
    developing for desktop platforms, there's no need to update
    Ren'Py.

**6.12.1.1501**: May 04, 2011
    Updated release. Mistakes were made in the update release process, leading
    to a version of Ren'Py that could not switch between windowed and fullscreen
    modes. (Among other problems.) Those problems have been fixed.

**6.12.1.1500**: May 03, 2011
    Updated release. This fixes a bug that prevented Ren'Py from running on
    systems with very old ATI drivers.

**6.12.1.1499**: May 02, 2011
    Final release. Fixes a bug with screenshots.

**6.12.1.1497**: April 30, 2011
    Fixes display of exceptions during init code. Allows the contents of
    viewports to be displayed by the shift+I style inspector. Populates
    config.archives in ascii order.

**6.12.1.1493**: April 24, 2011
    Bug fixes involving say with image attributes.
    Added config.say_attribute_transition as a way to invoke a transition
    when the image is changed by a say with image attributes, in response
    to feedback from the first users of the feature.

**6.12.1.1487**: April 24, 2011
    First public pre-release.
""",

    aside_html="""\
        <object width="380" height="238">
            <param name="movie" value="http://www.youtube.com/v/_MRDp2RHGEc?fs=1&amp;hl=en_US&amp;rel=0"></param>
            <param name="allowFullScreen" value="true"></param>
            <param name="allowscriptaccess" value="always"></param>
            <embed src="http://www.youtube.com/v/_MRDp2RHGEc?fs=1&amp;hl=en_US&amp;rel=0" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="380" height="238"></embed>
        </object>

    <i><a href="http://sonia-leong.livejournal.com/200681.html">Let Me Save You! Your Faithful Companion</a></i> time-lapse creation screencast. Courtesy Sonia Leong.
"""
    )


Release(
    prerelease=False,
    version="6.12.0",
    name="Positronic Brain",
    revision="e",
    date="February 7, 2011",
    exe=21,
    zip=27,
    bz2=25,
    android=True,
    deps="6.11.0",
    announcement="""\
Ren'Py 6.12.0 "Positronic Brain" is a major release of Ren'Py. This
release adds suport for the Android platform, allowing Ren'Py games to
run on millions of smartphones and tablets. It's possible to package
Ren'Py games and distribute them through the Android market.

On all platforms, this release benefits from improved performance in
the areas of image prediction and OpenGL rendering. New functionality
includes sprites, mouse hover areas, and drag-and-drop. The screen
support added in 6.11 has been improved, and new games now use screens
by default.
""",
    history="""\
**2011-02-07**
    Final release (6.12.0e). Improves the default screen and fixes
    bugs.

**2011-02-05**
    Fourth pre-release (6.12.0d). Adds main menu prediction, fixes
    screen bugs, improves the default screens, and fixes documentation.

**2011-02-03**
    Third pre-release (6.12.0c). Updates are documented `here <http://lemmasoft.renai.us/forums/viewtopic.php?f=32&t=9207&p=121140#p121140>`_.

**2011-01-30**
    Second pre-release (6.12.0b). Fixes the following bugs:

    * Ren'Py did not work for non-ASCII languages.
    * libGLEW was not distributed on Linux.
    * Could not load savegames that had Renders leak to them.
    * Frames had visual artifacts on the software renderer.

**2011-01-29**
    Initial pre-release (6.12.0a).
""",
    aside_html="""\
<img src="/static/6.12.0small.jpg" width="380" height="295">
"""
    )


Release(
    version="6.11.2",
    name="It Takes Two",
    revision="b",
    date="October 31, 2010",
    exe=20,
    zip=25,
    bz2=24,
    deps="6.11.0",
    announcement="""\
Ren'Py 6.11.2 "It Takes Two" is the second
minor release of the Ren'Py 6.11 series. The primary focus of this
release is to fix bugs found in previous releases. It also includes
four new themes, and updates the included jEdit text editor.
""",
    history="""\
**2010-10-31**
    Promoted 6.11.2b to final release.
**2010-10-26**
    Second pre-release (6.11.2b). Fixes a longstanding but unlikely bug with Frame.
**2010-10-24**
    Initial pre-release (6.11.2a).
""",
    aside_html="""\
        <object width="380" height="238">
            <param name="movie" value="http://www.youtube.com/v/2qrPIdRhv_Y?fs=1&amp;hl=en_US&amp;rel=0"></param>
            <param name="allowFullScreen" value="true"></param>
            <param name="allowscriptaccess" value="always"></param>
            <embed src="http://www.youtube.com/v/2qrPIdRhv_Y?fs=1&amp;hl=en_US&amp;rel=0" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="380" height="238"></embed>
        </object>
"""

    )

# Pre-web releases.
WikiRelease(version="6.11.1", name="Done in One", date="September 17, 2010")
WikiRelease(version="6.11.0", name="It Goes to Eleven", date="August 19, 2010")
WikiRelease(version="6.10.2", name="Fixing a Hole", date="January 24, 2010")
WikiRelease(version="6.10.1", name="I Can See Clearly Now", date="December 16, 2009")
WikiRelease(version="6.10.0", name="You Ain't Seen Nothing Yet", date="November 18, 2009")
WikiRelease(version="6.9.3", name="Road to Recovery", date="August 3, 2009")
WikiRelease(version="6.9.2", name="Roadside Attraction", date="May 3, 2009")
WikiRelease(version="6.9.1", name="Rest Stop", date="April 18, 2009")
WikiRelease(version="6.9.0", name="The Long and Winding Road", date="March 9, 2009")
WikiRelease(version="6.8.1", name="Heroic Hexameter", date="December 1, 2008")
WikiRelease(version="6.8.0", name="Good News", date="October 25, 2008")
WikiRelease(version="6.7.1", name="Apple Juice", date="September 28, 2008")
WikiRelease(version="6.7.0", name="Splines or Skins", date="September 10, 2008")
WikiRelease(version="6.6.3", name="Bender", date="July 25, 2008")
WikiRelease(version="6.6.2", name="But I Get Up Again", date="May 14, 2008")
WikiRelease(version="6.6.1", name="T-Minus", date="March 15, 2008")
WikiRelease(version="6.6.0", name="Layouts and themes and bears, oh my.", date="February 10, 2008")
WikiRelease(version="6.5.0", name="Breakeven", date="December 29, 2007")
WikiRelease(version="6.4.0", name="Character Actor", date="November 14, 2007")
WikiRelease(version="6.3.3", name="Spiral Energy", date="October 9, 2007")
WikiRelease(version="6.3.2", name="Wheel of Fire", date="August 15, 2007")
WikiRelease(version="6.3.1", name="Clairvoyant Koala", date="July 15, 2007")
WikiRelease(version="6.3.0", name="Giving Blood", date="June 21, 2007")
WikiRelease(version="6.2.0", name="Shpadoinkle Day", date="April 26, 2007")
WikiRelease(version="6.1.1", name="Snow Bunny", date="March 25, 2007")
WikiRelease(version="6.1.0", name="Once More Unto the Breach", date="March 6, 2007")
WikiRelease(version="6.0.0", name="The World Creates", date="February 17, 2007")
WikiRelease(version="5.6.7", name="Make a Statement", date="February 8, 2007")
WikiRelease(version="5.6.6", name="Mighty-X", date="January 12, 2007")
WikiRelease(version="5.6.5", name="Hachiko", date="December 18, 2006")
WikiRelease(version="5.6.4", name="Penguin Parity", date="November 17, 2006")
WikiRelease(version="5.6.3", name="Demo Party", date="November 11, 2006")
WikiRelease(version="5.6.2", name="New World Order", date="October 5, 2006")
WikiRelease(version="5.6.1", name="Community Service", date="September 13, 2006")
WikiRelease(version="5.6.0", name="Community Property", date="September 5, 2006")
WikiRelease(version="5.5.4", name="Engine X", date="August 7, 2006")
WikiRelease(version="5.5.3", name="The Intrigues of Upcoming Releases", date="July 16, 2006")
WikiRelease(version="5.5.2b", name="The Boredom of Bugfixing III", date="June 10, 2006")
WikiRelease(version="5.5.2a", name="The Boredom of More Bugfixing", date="June 1, 2006")
WikiRelease(version="5.5.2", name="The Boredom of Bugfixing", date="June 1, 2006")
WikiRelease(version="5.5.1", name="The Sighs of Hyperlinks", date="May 30, 2006")
WikiRelease(version="5.5.0", name="The Melancholy of Themeable Interfaces", date="April 30, 2006")
WikiRelease(version="5.4.5", name="Graf Eisen", date="April 7, 2006")
WikiRelease(version="5.4.4", name="Congrats Kathryn and mikey", date="March 12, 2006")
WikiRelease(version="5.4.3", name="Reinforce", date="March 8, 2006")
WikiRelease(version="5.4.2", name="Raging Heart", date="February 18, 2006")
WikiRelease(version="5.4.1", name="Bardiche", date="February 12, 2006")
WikiRelease(version="5.4.0", name="Death Clock", date="February 4, 2006")
WikiRelease(version="5.3.3", name="Particle Man", date="January 12, 2006")
WikiRelease(version="5.3.2", name="New Lang Syne", date="December 27, 2005")
WikiRelease(version="5.3.1", name="Joy To The World", date="December 25, 2005")
WikiRelease(version="5.3.0", name="Another Inked Finger", date="December 13, 2005")
WikiRelease(version="5.2.1", name="From Here On...", date="November 29, 2005")
WikiRelease(version="5.2.0", name="Skuld's Hammer", date="November 21, 2005")
WikiRelease(version="5.1.6", name="Artist's Alley", date="November 13, 2005")
WikiRelease(version="5.1.5", name="Palindrome", date="October 25, 2005")
WikiRelease(version="5.1.4", name="Love Simulation Syndrome", date="October 14, 2005")
WikiRelease(version="5.1.3", name="Sed Nobis", date="September 24, 2005")
WikiRelease(version="5.1.2", name="Click Already!", date="September 14, 2005")
WikiRelease(version="5.1.1", name="Katamari Bugfix", date="September 8, 2005")
WikiRelease(version="5.1.0", name="Paper Anniversary", date="August 24, 2005")
WikiRelease(version="5.0.1", name="Return to...", date="July 26, 2005")
WikiRelease(version="5.0", name="Spider", date="June 10, 2005")
WikiRelease(version="4.8.10", name="Zenith", date="June 23, 2005")
WikiRelease(version="4.8.9", name="Seagull", date="June 17, 2005")
WikiRelease(version="4.8.8", name="Cedar", date="June 12, 2005")
WikiRelease(version="4.8.7", name="American Eagle", date="June 9, 2005")
WikiRelease(version="4.8.6", name="Molly Brown", date="May 29, 2005")
WikiRelease(version="4.8.5", name="Faith 8", date="May 26, 2005")
WikiRelease(version="4.8.4", name="Sigma 8", date="May 13, 2005")
WikiRelease(version="4.8.3", name="Aurora 8", date="May 7, 2005")
WikiRelease(version="4.8.2a", name="", date="May 3, 2005")
WikiRelease(version="4.8.2", name="Friendship 8", date="May 2, 2005")
WikiRelease(version="4.8.1", name="Liberty Bell 8", date="April 26, 2005")
WikiRelease(version="4.8", name="Freedom 8", date="April 22, 2005")
WikiRelease(version="4.7.2", name="", date="April 2, 2005")
WikiRelease(version="4.7.1", name="The Clock is Running!", date="February 27, 2005")
WikiRelease(version="4.7", name="", date="February 14, 2005")
WikiRelease(version="4.6.1", name="", date="February 10, 2005")
WikiRelease(version="4.6", name="Start your Engines!", date="February 8, 2005")
WikiRelease(version="4.5", name="Inked Finger", date="February 5, 2005")
WikiRelease(version="4.4.2", name="", date="January 16, 2005")
WikiRelease(version="4.4", name="Christmas Bonus", date="December 25, 2004")
WikiRelease(version="4.3.1", name="", date="December 14, 2004")
WikiRelease(version="4.3", name="", date="December 11, 2004")
WikiRelease(version="4.2", name="", date="September 25, 2004")
WikiRelease(version="4.1", name="", date="September 12, 2004")
WikiRelease(version="4.0", name="", date="September 6, 2004")
WikiRelease(version="4pr1", name="Preview Release 1", date="August 24, 2004")

# The currrent pre-release and release.
prerelease = None
current = None

# A map from version to the release object. Used to get information about
# a particular release.
release_version = { }

# All final releases.
final_releases = [ ]

for i in releases:
    if i.prerelease:
        if not i.invisible:
            prerelease = prerelease or i
    else:
        current = current or i
        final_releases.append(i)

    if not i.wiki:
        release_version[i.version] = i

for i in aliases:
    release_version[i.old] = release_version[i.new]

for n, i in enumerate(final_releases):
    i.ordinal = len(final_releases) - n
