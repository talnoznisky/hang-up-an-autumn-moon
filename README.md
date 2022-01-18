# Hang up an Autumn Moon

```
I almost forgot
To hang up an autumn moon
Over the mountain.
- Richard Wright
```

`hang-up-an-autumn-moon` is an oracular CLI based on haiku by Richard Wright.
This project is currently beta-ish. 

Web version here: [https://hangupanautumnmoon.com/](https://hangupanautumnmoon.com/)

### Requires
* Python 3

## Installation
### Using Pip
```bash
$ pip install hang-up-an-autumn-moon
```
### Manual
```bash
$ git clone https://github.com/talnoznisky/hang-up-an-autumn-moon
$ cd hang-up-an-autumn-moon
$ python setup.py install
```

## Authors
tal.noznisky@gmail.com

## License
This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments
* ['Haiku: This Other World' by Richard Wright](https://www.publishersweekly.com/978-1-55970-445-8) Yoshinobu Hakatuni, Editor
* Anton Semjenov\'s [randomart implementation](https://github.com/ansemjo/randomart)

## Guidebook 
hang-up-an-autumn moon is an oracular CLI based on the late haiku of Richard Wright

Quick start:
Run `hang-up-an-autumn-moon oracle` to receive a spread of cards pseudo-randomly
generated from the haiku. Select a card to recieve your oracle. 

Use the --sparrow-mode flag to limit the oracle to haiku about sparrows.

Methodology:
When summoned, the oracle randomly selects three haiku from an internal corpus 
of haiku by Richard Wright. Then the oracle creates a little doodle of each haiku
by passing segment of the text to an algorithmic art generator. The querent gets
a three-card spread of the doodles and must select one. The oracle returns the card's
full haiku and a judgment to help frame the querent's insight into the haiku. 

Source material:
The oracle is based on a corpus of haiku by Richard Wright. Each haiku is attributed
with a mode, either sparrow or intensifier, and a pair of judgments. The modes are 
similar to the major and minor arcana of the Tarot. Sparrow cards represent 
higher-order considerations and are actually all about sparrows. Intensifier cards 
speak to day-by-day concerns and their haikus tend to describe the intensification
of one natural element by another. The judgments also vary by mode: sparrow cards
offer single subjective nouns for framing the haiku; intensifier cards offer very
brief imperatives to help the querent ideate a course of action.