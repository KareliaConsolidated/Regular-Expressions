# Match: self, himself, herself, itself, myself, yourself, thyself
# Match both "virtue" and "virtues"
# Use quantified repetition to find the word that starts with "T" and has 12 letters
# Match all text inside quotation marks, but nothing that is not inside them
import re
with open('Emerson.txt') as file:
	pattern_01 = '\w*self'
	Emerson = file.read()
	result_01 = re.findall(pattern_01, Emerson)
	print(result_01)  # ['himself', 'thyself', 'itself', 'himself', 'yourself', 'himself', 'itself', 'myself', 'yourself', 'himself', 'itself', 'self', 'yourself', 'himself', 'itself', 'itself', 'self', 'self', 'itself', 'himself', 'himself', 'self', 'himself', 'yourself', 'self', 'itself', 'self', 'self', 'itself', 'myself', 'myself', 'myself', 'myself', 'self', 'yourself', 'myself', 'himself', 'himself', 'himself', 'self', 'himself', 'self', 'itself', 'self', 'self', 'self', 'himself', 'himself', 'self', 'itself', 'yourself', 'himself', 'itself', 'himself', 'self', 'itself', 'himself', 'himself', 'himself', 'himself', 'yourself']

	pattern_02 = 'virtues?'
	result_02 = re.findall(pattern_02, Emerson)
	print(result_02) # ['virtue', 'virtues', 'virtues', 'virtue', 'virtue', 'virtue', 'virtue', 'virtue', 'virtue', 'virtue', 'virtue', 'virtue', 'virtue', 'virtue', 'virtue', 'virtue']

	pattern_03 = 'T\w{11}'
	result_03 = re.findall(pattern_03, Emerson)
	print(result_03) # ['Tranquillity']

	pattern_04 = "(.|\n)+?"
	result_04 = re.findall(pattern_04, Emerson)
	print(result_04) # ['"Ne te quaesiveris extra."', '"But these impulses may be from below, not from above."', '"They do not seem to me to be such; but if I am the devil\'s child, I will live then from the devil."', '"Go love thy infant; love thy wood-chopper; be good-natured and modest; have that grace; and never varnish your hard, uncharitable ambition with this incredible tenderness for black folk a thousand miles off. Thy love afar is spite at home."', '"the foolish face of praise,"', '"the height of Rome;"', '"I think,"', '"I am,"', '"Come out unto us."', '"What we love that we have, but by desire we bereave ourselves of the love."', '"studying a profession,"', '"His hidden meaning lies in our endeavors; Our valors are our best gods."', '"To the persevering mortal,"', '"the blessed Immortals are swift."', '"Let not God speak to us, lest we die. Speak thou, speak any man with us, and we will obey."', '"It must be somehow that you stole the light from us."', '"without abolishing our arms, magazines, commissaries and carriages, until, in imitation of the Roman custom, the soldier should receive his supply of corn, grind it in his hand-mill and bake his bread himself."', '"Thy lot or portion of life,"', '"is seeking after thee; therefore be at rest from seeking after if."']