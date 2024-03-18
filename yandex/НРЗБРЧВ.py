def translate(text):
    global translated_text
    vowels = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н',
              'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ь']
    vowels_ = ''.join(vowels).upper()
    vowels.extend(vowels_)
    translated_text = ''
    previous = ''
    for i in text:
        if i in vowels or (i == ' ' and previous != ' ' and len(translated_text)):
            previous = i
            translated_text += i
