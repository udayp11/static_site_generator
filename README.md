# Static Site Generator

A lightweight static site generator built in **Python** and shell scripts that converts source content into static HTML pages using templates.

---

## 🌟 Live Demo

You can see a demo of the generated site here:  
[Live Demo Link](https://udayp11.github.io/static_site_generator/)  <!-- Replace with your deployed site -->

---

## 🧩 Features
- Converts Markdown content to HTML using a template
- Handles inline markdown elements (bold, italic, code, links, images)
- Generates pages recursively from a content directory
---


## 📂 Project Structure

- content/: Your Markdown source files (pages and blog posts)
- static/: Static assets to copy (CSS, images)
- docs/: Generated production site (served by GitHub Pages)
- src/: Python source for the generator
- template.html: HTML template with placeholders for Title and Content
- build.sh: Production build script
- main.sh: Local build script (optional)

---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.x installed on the system

 **Clone the repo**
 ```bash
git clone https://github.com/udayp11/static_site_generator.git 
```
```bash
cd static_site_generator
```
**Prepare your content**
- Add your **HTML/Markdown content files** inside the `content/` folder  
- Add your **images, CSS, and other assets** inside the `static/` folder  
- Modify template.html to change layout, header, footer, CSS links, etc.

The generator will process the files in `content/` and copy static files into the final `docs/` build folder.

## 🚀 Usage

### Build only

Generate the static site into the `docs/` folder:

- Production (build for GitHub Pages with base path “/REPO_NAME/”):


```bash
./build.sh 
```


### Build + Serve Locally

- Local (build to docs/ with base path “/”, then serve on http://localhost:8888):

```bash
./main.sh 
```

## Deployment(Github Pages)🌐

1. ✅ Push the repo to GitHub  
2. ✅Go to **Settings > Pages**  
3. ✅Select branch: `main` and folder: `/docs`  
4. 🚀Your site will be live at: 
 https://username.github.io/repo-name/

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.


## License

[MIT](https://choosealicense.com/licenses/mit/)

