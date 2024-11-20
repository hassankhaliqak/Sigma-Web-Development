import os

# Function to create folders and files
def create_folders_and_files(start, end):
    for i in range(start, end + 1):
        folder_name = f"video{i}"
        os.makedirs(folder_name, exist_ok=True)
        
        # Create index.html with linked CSS and JS
        with open(os.path.join(folder_name, 'index.html'), 'w') as html_file:
            html_file.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Video {i}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Welcome to Video {i}</h1>
    <script src="script.js"></script>
</body>
</html>""")
        
        # Create style.css
        with open(os.path.join(folder_name, 'style.css'), 'w') as css_file:
            css_file.write("""body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    margin: 0;
    padding: 0;
    text-align: center;
}""")
        
        # Create script.js
        with open(os.path.join(folder_name, 'script.js'), 'w') as js_file:
            js_file.write("""document.addEventListener('DOMContentLoaded', function() {
    console.log('Video page loaded');
});""")

# Create folders and files from video14 to video100
create_folders_and_files(14, 100)