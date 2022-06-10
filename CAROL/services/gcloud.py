from google.cloud import vision

def detect_text(image_file):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()
    print("before type")

    response = client.text_detection(image=image_file ,image_context={"language_hints": ["es"]})  # Bengali

    texts = response.text_annotations
    print('Texts:')

    words_dict={}
    words_list=[]
    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

        words_dict[text.description]=list(vertices)
        words_list.append(text.description)
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    del words_list[0]
    return words_list
