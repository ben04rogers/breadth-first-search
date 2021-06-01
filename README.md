# CAB203 Breath First Search Problem
CAB203 problem that uses breadth first search to caculate minimum distance from one person to every other person in a family tree. 

## Problem Description

Bob lives in an isolated community on board a generation ship — a spaceship travelling to a distant starover  several  lifetimes.   Naturally  over  the  generations  the  community  has  come  a  point  where  everybodyis related to everybody.  Bob has recently become interested in genealogy and has constructed a completefamily tree for the community going back to the first generation, using the ship’s meticulous records.  Histree records the parents and children of every person, from which it is possible to work out how any twopeople on the ship are related.

Since then Bob has become obsessed with understanding how he is related to the other people on the ship,and these relationships are quite complicated!  For example, Alice is not only his second cousin (his mother’sfather’s  mother’s  son’s  daughter’s  daughter)  but  also  his  first  cousin  once  removed  (his  father’s  mother’smother’s son’s daughter), in additional to numerous other relationships.

Bob has decided to simplify his understanding of these relationships by adding annotations to his familytree by marking the parent-child relationships that link people most directly to him.  Here he considers a parent-child relationship (which we’ll call astep) to be direct, and other relationships are measured by howmany parent-child relations it takes to get from a person back to Bob.  For example, Alice’s relationship toBob takes 5 steps via Alice’s father, and 6 steps via her mother, so — assuming there are no more directrelationships — Bob’s annotated tree will mark the relationship between Alice and her father, and there willbe no mark on the relationship between Alice and her mother.  This way Bob can quickly see the most directrelationship that he has with any person.

Bob  realises  that  there  may  be  more  than  one  relationship  between  himself  and  another  person  that  areequally direct, in which case he is happy with any one of them.  Further, Bob has realised that his definitionof relationship includes some cases that others might not consider as being a family relationship, particularlythrough  half-siblings.   However,  Bob  has  decided  to  stick  with  his  definition. Basically,  just  don’t  worryabout these cases.

Help Bob to create his simplified family tree:  given the complete family tree, find a simplified tree wherethere is a unique way of relating Bob to each other person, and that relationship is most direct among allpossible relationships in the complete family tree.

Bob’s family tree is in the form ofcards.  Each card lists a person’s name, father, mother, and children (plusother information such as date of birth that we can ignore here.)  Bob would like to have new cards thatshow the same information, but have a * in front of the names of people where the relationship needs to bemarked.  For example, on Alice’s card, Alice’s father’s name will have a * in front, and on Alice’s Father’scard there will be a * in front of Alice’s name.
