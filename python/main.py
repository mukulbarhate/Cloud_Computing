import json
import base64
from PIL import Image
from io import BytesIO

def lambda_handler(event, context):
    # Extract the base64 image and zoom factor from the event
    image_base64 = event.get('image_base64', '')
    zoom_factor = float(event.get('zoom_factor', 1.0))
    
    if not image_base64:
        return {
            'statusCode': 400,
            'body': json.dumps('Image data not provided')
        }

    try:
        # Decode the base64 image
        image_data = base64.b64decode(image_base64)
        image = Image.open(BytesIO(image_data))

        # Get the original size
        width, height = image.size
        
        # Calculate the new size
        new_width = int(width * zoom_factor)
        new_height = int(height * zoom_factor)

        # Resize the image (zoom in)
        zoomed_image = image.resize((new_width, new_height), Image.LANCZOS)

        # Convert the zoomed image back to base64
        buffer = BytesIO()
        zoomed_image.save(buffer, format="PNG")
        zoomed_image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

        return {
            'statusCode': 200,
            'body': json.dumps({
                'zoomed_image_base64': zoomed_image_base64
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error processing image: {str(e)}")
        }