import runway
from runway.data_types import image
from image_composition import Image_composition

@runway.setup(options={})
def setup(opts):
    model = Image_composition()
    return model

@runway.command(name='composite',
                inputs={ 'background': image(channels=3), 'foreground': image(channels=4) },
                outputs={ 'composition': image(channels=3) },
                description='Generates a composition of the two input images')
def generate(model, args):
    output_image = model.run_on_input(args['background'],args['foreground'])
    return {
        'composition': output_image
    }

if __name__ == '__main__':
    runway.run(host='0.0.0.0', port=9000)

