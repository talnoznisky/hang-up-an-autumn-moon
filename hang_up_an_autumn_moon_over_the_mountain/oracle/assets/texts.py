tab_space = '   '

project_credit = """
All haikus by Richard Wright, taken from "This Other World," 
a compendium of haiku he wrote in sickness before his death.

The randomart generation code is forked and modified from Anton Semjonov implementation:\n
https://github.com/ansemjo/randomart
"""

guidebook_text = """
I almost forgot\\To hang up an autumn moon\\Over the mountain.\n
- Richard Wright

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
with a mode, either sparrow or hyperdrive, and a pair of judgments. The modes are 
similar to the major and minor arcana of the Tarot. Sparrow cards represent 
higher-order considerations and are actually all about sparrows. Hyperdrive cards 
speak to day-by-day concerns and their haikus tend to describe the intensification
of one natural element by another. The judgments also vary by mode: sparrow cards
offer single subjective nouns for framing the haiku; hyperdrive cards offer very
brief imperatives to help the querent ideate a course of action.
"""

cards = [
    {
        'text':  f"{tab_space}On a scarecrow's head\nA sparrow braces itself\n{tab_space}Against the spring wind.",
        'oracle': ['Spontaneity', 'Safety'],
        'mode': 'sparrow'
    },
    {
        'text': f"{tab_space}From the cherry tree\nTo the roof of the red barn\n{tab_space}A cloud of sparrows flew.",
        'oracle': ['Manifestation', 'Distraction'],
        'mode': 'sparrow'
    },
    {
        'text': f"{tab_space}A magnolia\nFell amid fighting sparrows\n{tab_space}Putting them to flight.",
        'oracle': ['Excitement', 'Vulnerability'],
        'mode': 'sparrow'
    },
    {
        'text': f"{tab_space}Does the sparrow know\nThat it is upon my roof\n{tab_space}That he is hopping?",
        'oracle': ['Passivity', 'Guilt'],
        'mode': 'sparrow'
    },
    {
        'text': f"{tab_space}It is not outdoors\nThat the baby sparrow cheeps\n{tab_space}But here in the house!",
        'oracle': ['Suspicion', 'Delight'],
        'mode': 'sparrow'
    },
    {
        'text': f"{tab_space}All right, You Sparrows;\nThe sun has set and you can now\n{tab_space}Stop your chattering!",
        'oracle': ['Exhaustion', 'Renewal'],
        'mode': 'sparrow'
    },
    {
        'text': f"{tab_space}The day is so long\nThat even noisy sparrows\n{tab_space}Fall strangely silent.",
        'oracle': ['Conciliation', 'Caution'],
        'mode': 'sparrow'
    },
    {
        'text': f"{tab_space}For some strange reason\nSparrows are congregating\n{tab_space}In an old rose bush.",
        'oracle': ['Desire', 'Confusion'],
        'mode': 'sparrow'
    },
    {
        'text': f"{tab_space}Shrilling sparrows\nAre sheathing the waterfall\n{tab_space}With glittering light.",
        'oracle': ['Insightfulness', 'Achievement'],
        'mode': 'sparrow'
    },
    {
        'text': f"{tab_space}I slept so long and sound\nBut I did not know why until\n{tab_space}I saw the snow outside.",
        'oracle': ['Plan something', 'Rest first'],
        'mode': 'hyperdrive'
    },
    {
        'text': f"{tab_space}Over spring mountains\nA star ends the paragraph\n{tab_space}Of a thunderstorm.",
        'oracle': ['Make peace', 'Measure change'],
        'mode': 'hyperdrive'
    },
    {
        'text': f"{tab_space}From a tenement\nThe blue jazz of a trumpet\n{tab_space}Weaving autumn mists.",
        'oracle': ['Live seasonally', 'Combine sensitivities'],
        'mode': 'hyperdrive'
    },
    {
        'text': f"{tab_space}The chill autumn dusk\nGrows colder as yellow lights\n{tab_space}Come on in skyscrapers",
        'oracle': ['Leave work', 'Accept diminishment'],
        'mode': 'hyperdrive'
    },
    {
        'text': f"{tab_space}The ocean's soft sound\nLifts the toll of a far bell\n{tab_space}To the half-seen stars.",
        'oracle': ['Contain excitement', 'Gaze widely'],
        'mode': 'hyperdrive'
    },
    {
        'text': f"{tab_space}A cathedral bell\nDimming the river water\n{tab_space}In the autumn dusk.",
        'oracle': ['Reappraise constants', 'Leave soon'],
        'mode': 'hyperdrive'
    },
    {
        'text': f"{tab_space}A layer of snow\nIs pulling the mountains nearer\n{tab_space}Making them smaller.",
        'oracle': ['Tighten boundaries', 'Lead intimacy'],
        'mode': 'hyperdrive'
    },
    {
        'text': f"{tab_space}One caw of a crow\nTints all of the fallen leaves\n{tab_space}A deeper yellow.",
        'oracle': ['Dress different', 'Look back'],
        'mode': 'hyperdrive'
    },
    {
        'text': f"{tab_space}The summer rainstorm \nDrenches chickens in the field\n{tab_space}Making them smaller.",
        'oracle': ['Absorb influences', 'Accept less'],
        'mode': 'hyperdrive'
    },
    {
        'text': f"{tab_space}Departing wild geese\nAre fanning the moon brighter\n{tab_space}With their tireless wings.",
        'oracle': ['Invent holidays', 'Never quit'],
        'mode': 'hyperdrive'
    },
    {
        'text': f"{tab_space}An empty seashore:\nTaking a long summer with it,\n{tab_space}A departing train.",
        'oracle': ['Leave alone', 'Create attachments'],
        'mode': 'hyperdrive'
    },
    {
        'text': f"{tab_space}The big light in the fog\nWas but a little lantern\n{tab_space}When we came to it.",
        'oracle': ['Confront honesty', 'Characterize spaces'],
        'mode': 'hyperdrive'
    },
    {
        'text': f"{tab_space}I am positive\nThat this is the same spring wind\n{tab_space}That I felt yesterday.",
        'oracle': ['Doubt hype', 'Recognize renewals'],
        'mode': 'hyperdrive'
    }
]
    

