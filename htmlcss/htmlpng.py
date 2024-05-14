from PIL import Image, ImageDraw, ImageFont
import random
import textwrap
import os

# Define image properties
width, height = 4096, 4096
tag_font_size = 480
desc_font_size = 160
font_path = "Ubuntu-Bold.ttf"  # Update this path to the location of your Arial font
padding = 200  # Padding around the text

text_file = open("color_data.txt", "a")

# Define CSS colors as RGB tuples
css_colors_rgb = {
    "AliceBlue": (240, 248, 255),
    "AntiqueWhite": (250, 235, 215),
    "Aqua": (0, 255, 255),
    "Aquamarine": (127, 255, 212),
    "Azure": (240, 255, 255),
    "Beige": (245, 245, 220),
    "Bisque": (255, 228, 196),
    "Black": (0, 0, 0),
    "BlanchedAlmond": (255, 235, 205),
    "Blue": (0, 0, 255),
    "BlueViolet": (138, 43, 226),
    "Brown": (165, 42, 42),
    "BurlyWood": (222, 184, 135),
    "CadetBlue": (95, 158, 160),
    "Chartreuse": (127, 255, 0),
    "Chocolate": (210, 105, 30),
    "Coral": (255, 127, 80),
    "CornflowerBlue": (100, 149, 237),
    "Cornsilk": (255, 248, 220),
    "Crimson": (220, 20, 60),
    "Cyan": (0, 255, 255),
    "DarkBlue": (0, 0, 139),
    "DarkCyan": (0, 139, 139),
    "DarkGoldenRod": (184, 134, 11),
    "DarkGray": (169, 169, 169),
    "DarkGreen": (0, 100, 0),
    "DarkKhaki": (189, 183, 107),
    "DarkMagenta": (139, 0, 139),
    "DarkOliveGreen": (85, 107, 47),
    "DarkOrange": (255, 140, 0),
    "DarkOrchid": (153, 50, 204),
    "DarkRed": (139, 0, 0),
    "DarkSalmon": (233, 150, 122),
    "DarkSeaGreen": (143, 188, 143),
    "DarkSlateBlue": (72, 61, 139),
    "DarkSlateGray": (47, 79, 79),
    "DarkTurquoise": (0, 206, 209),
    "DarkViolet": (148, 0, 211),
    "DeepPink": (255, 20, 147),
    "DeepSkyBlue": (0, 191, 255),
    "DimGray": (105, 105, 105),
    "DodgerBlue": (30, 144, 255),
    "FireBrick": (178, 34, 34),
    "FloralWhite": (255, 250, 240),
    "ForestGreen": (34, 139, 34),
    "Fuchsia": (255, 0, 255),
    "Gainsboro": (220, 220, 220),
    "GhostWhite": (248, 248, 255),
    "Gold": (255, 215, 0),
    "GoldenRod": (218, 165, 32),
    "Gray": (128, 128, 128),
    "Green": (0, 128, 0),
    "GreenYellow": (173, 255, 47),
    "HoneyDew": (240, 255, 240),
    "HotPink": (255, 105, 180),
    "IndianRed": (205, 92, 92),
    "Indigo": (75, 0, 130),
    "Ivory": (255, 255, 240),
    "Khaki": (240, 230, 140),
    "Lavender": (230, 230, 250),
    "LavenderBlush": (255, 240, 245),
    "LawnGreen": (124, 252, 0),
    "LemonChiffon": (255, 250, 205),
    "LightBlue": (173, 216, 230),
    "LightCoral": (240, 128, 128),
    "LightCyan": (224, 255, 255),
    "LightGoldenRodYellow": (250, 250, 210),
    "LightGray": (211, 211, 211),
    "LightGreen": (144, 238, 144),
    "LightPink": (255, 182, 193),
    "LightSalmon": (255, 160, 122),
    "LightSeaGreen": (32, 178, 170),
    "LightSkyBlue": (135, 206, 250),
    "LightSlateGray": (119, 136, 153),
    "LightSteelBlue": (176, 196, 222),
    "LightYellow": (255, 255, 224),
    "Lime": (0, 255, 0),
    "LimeGreen": (50, 205, 50),
    "Linen": (250, 240, 230),
    "Magenta": (255, 0, 255),
    "Maroon": (128, 0, 0),
    "MediumAquaMarine": (102, 205, 170),
    "MediumBlue": (0, 0, 205),
    "MediumOrchid": (186, 85, 211),
    "MediumPurple": (147, 112, 219),
    "MediumSeaGreen": (60, 179, 113),
    "MediumSlateBlue": (123, 104, 238),
    "MediumSpringGreen": (0, 250, 154),
    "MediumTurquoise": (72, 209, 204),
    "MediumVioletRed": (199, 21, 133),
    "MidnightBlue": (25, 25, 112),
    "MintCream": (245, 255, 250),
    "MistyRose": (255, 228, 225),
    "Moccasin": (255, 228, 181),
    "NavajoWhite": (255, 222, 173),
    "Navy": (0, 0, 128),
    "OldLace": (253, 245, 230),
    "Olive": (128, 128, 0),
    "OliveDrab": (107, 142, 35),
    "Orange": (255, 165, 0),
    "OrangeRed": (255, 69, 0),
    "Orchid": (218, 112, 214),
    "PaleGoldenRod": (238, 232, 170),
    "PaleGreen": (152, 251, 152),
    "PaleTurquoise": (175, 238, 238),
    "PaleVioletRed": (219, 112, 147),
    "PapayaWhip": (255, 239, 213),
    "PeachPuff": (255, 218, 185),
    "Peru": (205, 133, 63),
    "Pink": (255, 192, 203),
    "Plum": (221, 160, 221),
    "PowderBlue": (176, 224, 230),
    "Purple": (128, 0, 128),
    "RebeccaPurple": (102, 51, 153),
    "Red": (255, 0, 0),
    "RosyBrown": (188, 143, 143),
    "RoyalBlue": (65, 105, 225),
    "SaddleBrown": (139, 69, 19),
    "Salmon": (250, 128, 114),
    "SandyBrown": (244, 164, 96),
    "SeaGreen": (46, 139, 87),
    "SeaShell": (255, 245, 238),
    "Sienna": (160, 82, 45),
    "Silver": (192, 192, 192),
    "SkyBlue": (135, 206, 235),
    "SlateBlue": (106, 90, 205),
    "SlateGray": (112, 128, 144),
    "Snow": (255, 250, 250),
    "SpringGreen": (0, 255, 127),
    "SteelBlue": (70, 130, 180),
    "Tan": (210, 180, 140),
    "Teal": (0, 128, 128),
    "Thistle": (216, 191, 216),
    "Tomato": (255, 99, 71),
    "Turquoise": (64, 224, 208),
    "Violet": (238, 130, 238),
    "Wheat": (245, 222, 179),
    "White": (255, 255, 255),
    "WhiteSmoke": (245, 245, 245),
    "Yellow": (255, 255, 0),
    "YellowGreen": (154, 205, 50)
}

# Define a dictionary with HTML tags and their descriptions
html_tags_dict = {
    "<a>": "Defines a hyperlink.",
    "<abbr>": "Defines an abbreviation or an acronym, providing a full term or explanation.",
    "<acronym>": "Defines an acronym. Obsolete in HTML5, use <abbr> instead.",
    "<address>": "Specifies contact information for the author/owner of a document or an article.",
    "<animate>": "Defines an animation that applies to SVG elements. Part of SVG, not standard HTML.",
    "<animatemotion>": "Causes an element to move along a motion path. Part of SVG animations.",
    "<animatetransform>": "Applies animated transformations to SVG elements. Part of SVG animations.",
    "<applet>": "Embeds a Java applet. Obsolete in HTML5, replaced by <object>.",
    "<area>": "Defines an area inside an image map that has predefined clickable areas.",
    "<article>": "Specifies independent, self-contained content that could stand alone from the rest of the content.",
 "<aside>": "Defines content aside from the page content, often used for sidebars, inserts, or non-essential information.",
    "<audio>": "Used to embed sound content in documents, allowing playback of audio files.",
    "<b>": "Renders text in boldface, used to draw attention without implying any added importance or urgency.",
    "<base>": "Specifies the base URL/target for all relative URLs in a document, setting a common base for all links and references within the page.",
    "<basefont>": "Obsolete. Was used to specify a default font size, color, and face for all text in a document.",
    "<bdi>": "Isolates a part of text that might be formatted in a different direction from other text outside it, useful for user-generated content.",
    "<bdo>": "Overrides the current text direction, allowing manual control over text directionality (left-to-right or right-to-left).",
    "<bgsound>": "Obsolete and non-standard. Was used to specify background sound on a web page.",
    "<big>": "Obsolete. Was used to increase the font size of a text, making it larger than the surrounding text.",
    "<blink>": "Obsolete and non-standard. Was used to create blinking text, considered problematic for accessibility and usability.",
"<blockquote>": "Defines a section that is quoted from another source, often used for longer quotes that take up an entire block of text.",
    "<body>": "Represents the content of an HTML document. There can be only one <body> element in a document.",
    "<br>": "Produces a line break in text, used to create a new line within an HTML document.",
    "<button>": "Defines a clickable button, which can be used in forms or anywhere in a document that needs simple, standard button functionality.",
    "<canvas>": "Used to draw graphics on the fly via scripting (usually JavaScript). It can be used for rendering graphs, game graphics, or other visual images on the fly.",
    "<caption>": "Specifies the caption (or title) of a table, which by default is centered above the table.",
    "<center>": "Obsolete. Was used to center-align text. Modern web design uses CSS to achieve text alignment.",
    "<cite>": "Defines the title of a creative work (e.g., book, poem, song, movie). It implies semantic importance and typically renders in italic.",
    "<code>": "Defines a piece of computer code. Its content is displayed in a monospace font, preserving spaces and line breaks.",
    "<col>": "Specifies column properties for each column within a `<colgroup>` element. It is used to apply CSS styles to entire columns, rather than individual table cells.",
"<colgroup>": "Used to group several `<col>` elements within a table. It allows you to define formatting on entire columns, rather than individual cells.",
    "<command>": "Obsolete. Was used to define a command button that users could invoke.",
    "<content>": "Obsolete, part of the Web Components specification, replaced by `<slot>` in the Shadow DOM v1.",
    "custom tags": "Not standard HTML tags. Developers can create custom elements for use in web documents as long as they include a hyphen in the name and are defined in the document or with a framework.",
    "<data>": "Allows you to associate a machine-readable equivalent with content. For example, to mark up a machine-readable date or currency value within human-readable text.",
    "<datalist>": "Contains a set of `<option>` elements that represent the permissible or recommended options available to choose from within other controls.",
    "<dd>": "Used in a description list (`<dl>`), where it follows a `<dt>` element and provides details about the term described by `<dt>`.",
    "<del>": "Represents text that has been deleted from the document. It often appears with the `<ins>` element to mark changes.",
    "<details>": "Used to specify additional details that the user can view or hide on demand. A common use case is a collapsible widget.",
    "<dfn>": "Represents the defining instance of a term in HTML. The content within `<dfn>` should be the term being defined.",
    "<dialog>": "Represents a dialog box or other interactive component, such as a modal, that can be shown or hidden.",
    "<dir>": "Obsolete. Was used to create a directory list, but it is now deprecated in favor of `<ul>`.",
    "<discard>": "Part of the SVG specification, used to discard elements to optimize performance. Not part of HTML.",
    "<div>": "A generic container for flow content, used to group elements for styling purposes or because they share attribute values, typically via CSS.",
    "<dl>": "Represents a description list, a container for `<dt>` (term/name) and `<dd>` (description) elements.",
    "<dt>": "Used in a description list (`<dl>`) to indicate the term being described.",
    "element": "Not a standard HTML element. In discussions, 'element' typically refers to any HTML tag in the document.",
    "<em>": "Emphasizes text, typically displayed in italic, indicating a stress emphasis of its contents.",
    "<embed>": "Defines a container for an external application or interactive content (a plug-in).",
    "<fieldset>": "Used to group several controls as well as labels (`<label>`) within a web form.",
"<colgroup>": "Defines a group of one or more columns in a table for formatting.",
    "<command>": "Obsolete. Was used to define a command button that users could invoke.",
    "<content>": "Not standard. Previously used in Web Components technology, now replaced by `<slot>` in the Shadow DOM.",
    "custom tags": "Used with Web Components; allows developers to create their own custom HTML tags with custom behavior and properties.",
    "<data>": "Associates a machine-readable equivalent with its content for user-defined data.",
    "<datalist>": "Contains a set of `<option>` elements that represent the permissible or recommended options to choose from in other controls.",
    "<dd>": "Defines the description, definition, or value part of a term in a description list (`<dl>`).",
    "<del>": "Defines text that has been deleted from a document.",
    "<details>": "Defines additional details that the user can view or hide on demand.",
    "<dfn>": "Represents the defining instance of a term.",
    "<dialog>": "Defines a dialog box or window that can be toggled by the user.",
    "<dir>": "Obsolete. Was used to create a directory list. Use `<ul>` instead.",
    "<discard>": "Not standard. No widely recognized implementation or usage.",
    "<div>": "Defines a division or a section in an HTML document, used as a container for HTML elements.",
    "<dl>": "Defines a description list, a list of terms and their corresponding descriptions.",
    "<dt>": "Defines a term/name in a description list (`<dl>`).",
    "element": "Not standard in the context of HTML elements. In Web Components, custom elements are defined using classes that extend HTMLElement.",
    "<em>": "Defines emphasized text, which is typically displayed in italics to denote emphasis.",
    "<embed>": "Defines a container for an external application or interactive content (a plug-in).",
    "<fieldset>": "Groups related elements and labels within a web form.",
    "<figcaption>": "Defines a caption for a `<figure>` element.",
    "<figure>": "Specifies self-contained content, like illustrations, diagrams, photos, code listings, etc., often with a caption (`<figcaption>`).",
    "<font>": "Obsolete. Was used to define font size, color, and face for text. Use CSS instead.",
    "<footer>": "Defines a footer for a document or a section, typically containing authorship information, copyright notices, contact information, and other related details.",
    "<form>": "Defines an HTML form for user input, containing form elements such as text fields, checkboxes, radio buttons, and submit buttons.",
    "<frame>": "Obsolete. Defined a particular area within a `<frameset>` where a document could be displayed. Use `<iframe>` or CSS instead for layouts.",
    "<frameset>": "Obsolete. Used to define a collection of frames or framesets. Replaced by CSS for layout.",
    "<h1>-<h6>": "Define HTML headings, `<h1>` being the highest level and `<h6>` the lowest.",
    "<head>": "Contains meta-information about the document, such as `<title>`, `<style>`, and `<meta>` tags.",
    "<header>": "Defines a header for a document or a section, typically containing introductory content or a set of navigational links.",
    "<hgroup>": "Obsolete. Was used to group a set of `<h1>`–`<h6>` elements when a section has multiple headings.",
    "<hr>": "Represents a thematic break between paragraph-level elements, for example, a change of scene in a story, or a shift of topic within a section.",
    "<html>": "Defines the root of an HTML document and contains the document's structure (`<head>` and `<body>`).",
    "<i>": "Defines a part of text in an alternate voice or mood, or otherwise offset from the normal prose, typically displayed in italics.",
    "<iframe>": "Defines an inline frame that embeds another document within the current HTML document.",
"<img>": "Embeds an image in an HTML document.",
    "<input>": "Defines an input control.",
    "<ins>": "Defines a text that has been inserted into a document.",
    "<kbd>": "Defines keyboard input.",
    "<keygen>": "Obsolete. Was used to facilitate generation of key material, and submission of the public key as part of an HTML form.",
    "<label>": "Defines a label for an `<input>` element.",
    "<legend>": "Defines a caption for a `<fieldset>`, `<figure>`, or `<details>` element.",
    "<li>": "Defines a list item.",
    "<link>": "Defines the relationship between a document and an external resource, typically used to link to stylesheets.",
    "<main>": "Specifies the main content of a document.",
    "<map>": "Defines a client-side image map.",
    "<mark>": "Defines text that should be highlighted or marked for reference or notation purposes, often used to highlight a part of text.",
    "<marquee>": "Obsolete. Was used to create scrolling text or images. Modern web development uses CSS animations for similar effects.",
    "<menu>": "Defines a menu or list of commands, more recently being specified as a semantic way to represent a list of items that are commands or options.",
    "<menuitem>": "Obsolete. Was used to define a command/menu item that the user could invoke from a popup menu created with the `<menu>` element.",
    "<meta>": "Defines metadata about the HTML document, such as character set, page description, keywords, author of the document, and viewport settings.",
    "<meter>": "Represents a scalar measurement within a known range, or a fractional value; for example, disk usage or the relevance of a query result.",
    "<multicol>": "Obsolete and non-standard. Was proposed to allow multi-column layouts in HTML documents.",
    "<nav>": "Defines a set of navigation links. It is intended for sections of a page that provide navigation links.",
    "<nextid>": "Obsolete and non-standard. Was used in early HTML documents to help browsers with layout.",
    "<nobr>": "Obsolete and non-standard. Was used to prevent text from breaking into a new line.",
    "<noembed>": "Obsolete. Provides alternative content for users whose browsers do not support embedded content.",
    "<noframes>": "Obsolete. Provides alternative content for users whose browsers do not support frames.",
    "<noscript>": "Defines alternative content to be displayed to users who have disabled scripts in their browser or have a browser that doesn't support client-side scripting.",
    "<object>": "Defines an embedded object within an HTML document. It can be used to include various types of data and more complex multimedia elements.",
    "<ol>": "Defines an ordered list of items, typically rendered as a numbered list.",
    "<optgroup>": "Defines a group of related options in a drop-down list (`<select>` element).",
    "<option>": "Defines an option in a drop-down list within a `<select>` or `<datalist>` element.",
    "<output>": "Represents the result of a calculation or user action.",
    "<p>": "Defines a paragraph. It is a block-level element that contains text.",
    "<param>": "Defines parameters for an `<object>` element, used to configure the object or embed plugin features.",
    "portal": "Not officially part of the HTML specification. Potentially related to modern web APIs or frameworks.",
    "<picture>": "Allows for more flexible image delivery by defining multiple `<source>` elements for different display scenarios.",
    "plaintext": "Obsolete. Was used to render text plainly, without HTML interpretation. Modern HTML does not use this element.",
    "<pre>": "Defines preformatted text. Content within a `<pre>` element is displayed in a fixed-width font, and it preserves spaces and line breaks.",
    "<progress>": "Represents the progress of a task, such as downloading, uploading, or any other progress indication.",
    "<q>": "Defines a short inline quotation. Browsers typically surround the content with quotation marks.",
    "rb": "Used within `<ruby>` annotations as the base text component. Part of the Ruby annotation used for East Asian typographic layout.",
    "rp": "Used within `<ruby>` annotations to provide parentheses around a ruby text, for browsers that do not support ruby annotations.",
    "rt": "Defines an explanation or pronunciation of characters (for East Asian typography) within a `<ruby>` annotation.",
    "rtc": "Used to mark ruby text container for ruby text components in East Asian typography.",
    "<ruby>": "Represents a ruby annotation, used for East Asian typographic layout to provide pronunciation guides.",
    "<s>": "Renders text with a strikethrough, or a line through it. Used to indicate text that is no longer relevant or has been deleted.",
    "<samp>": "Defines sample output from a computer program. Typically, it's displayed in a monospace font.",
    "<script>": "Used to embed or reference executable code; this is typically used to embed or refer to JavaScript code.",
"search": "Not an HTML element on its own. Typically refers to `<input type='search'>`, which is used to define a search field.",
    "<section>": "Defines a section in a document, such as chapters, headers, footers, or any other sections of the document.",
    "<select>": "Creates a drop-down list for forms, allowing the user to select one or more options.",
    "set": "Not standard in HTML. In SVG, `<set>` is used to define a simple animation where one attribute changes to a new value over a specified duration.",
    "shadow": "Previously part of Web Components; `<shadow>` is used with Shadow DOM. Modern usage involves attaching a shadow DOM directly to an element via JavaScript.",
    "<slot>": "A placeholder inside a web component that you can fill with your own markup, which lets you create separate DOM trees and present them together.",
    "<small>": "Makes the text font size smaller; used to denote fine print or side comments.",
    "<source>": "Specifies multiple media resources for `<picture>`, `<audio>`, and `<video>` elements, allowing the browser to choose the most appropriate source.",
    "spacer": "Non-standard and obsolete. Was used to create space in a page layout; modern web design uses CSS for spacing.",
    "<span>": "A generic inline container for phrasing content, which does not inherently represent anything. It can be used to style elements with CSS or manipulate with JavaScript.",
    "<strike>": "Obsolete. Represents text that has been struck through with a line. Use the `<s>` or `<del>` elements instead.",
    "<strong>": "Indicates that its contents have strong importance, seriousness, or urgency. Browsers typically render the contents in bold type.",
    "<style>": "Contains style information for a document, or part of a document.",
    "<sub>": "Defines subscript text, appearing half a character below the normal line, and is sometimes rendered in a smaller font.",
    "<summary>": "Specifies a visible heading for a `<details>` element; the summary can be clicked to reveal or hide the details.",
    "<sup>": "Defines superscript text, appearing half a character above the normal line, and is sometimes rendered in a smaller font.",
    "<svg>": "Defines a container for SVG graphics. SVG is a language for describing 2D graphics in XML.",
# "search": Not an HTML tag but an input type. Use <input type="search"> for search fields.
    "<section>": "Defines a section in a document, such as chapters, headers, footers, or any other sections of the document.",
    "<select>": "Creates a drop-down list for selecting one or more options.",
    # "set": Not a standard HTML tag. Possibly confused with SVG's <set> element for animations.
    # "shadow": Part of the Web Components technology, specifically related to the Shadow DOM.
    "<slot>": "A placeholder inside a web component that you can fill with your own markup, which lets you create separate DOM trees and present them together.",
    "<small>": "Makes the text smaller in size compared to surrounding text, typically used for fine print or side comments.",
    "<source>": "Specifies multiple media resources for the <picture>, <audio>, or <video> elements, allowing the browser to choose the best fit.",
    # "spacer": Non-standard and obsolete. Was used to create space in layouts but CSS should be used for spacing.
    "<span>": "Defines a section in a document for styling purposes without conveying any special meaning.",
    "<strike>": "Deprecated. Represents text that has been struck through. Use the <del> or <s> tag instead.",
    "<strong>": "Indicates that its contents have strong importance, seriousness, or urgency. Browsers typically render the contents in bold.",
    "<style>": "Contains style information for a document, or part of a document.",
    "<sub>": "Defines subscript text, which appears half a character below the normal line.",
    "<summary>": "Defines a visible heading for a <details> element, which can be clicked to view or hide the <details> content.",
    "<sup>": "Defines superscript text, which appears half a character above the normal line.",
    "<svg>": "Defines a container for SVG graphics and allows you to define vector-based graphics in XML format.",
    "<table>": "Defines a table.",
    "<tbody>": "Groups the body content in a table.",
    "<td>": "Defines a cell in a table.",
    "<template>": "Holds content that is not to be rendered immediately when a page is loaded but may be instantiated subsequently during runtime.",
    "<textarea>": "Defines a multi-line text input control.",
    "<tfoot>": "Groups the footer content in a table.",
    "<th>": "Defines a header cell in a table.",
    "<thead>": "Groups the header content in a table.",
    "<time>": "Represents a specific period in time.",
    "<title>": "Defines the title of the document, shown in the browser's title bar or page's tab.",
    "<tr>": "Defines a row in a table.",
    "<track>": "Used as a child of the <audio> or <video> elements, and enables subtitles or captions.",
    "<tt>": "Deprecated. Represents teletype or monospaced text. Use CSS instead.",
    "<u>": "Represents non-textually underlined text, such as proper names in Chinese text, or for stylistic purposes.",
    "<ul>": "Defines an unordered list.",
    "<var>": "Represents a variable in a mathematical expression or a programming context.",
    "<video>": "Embeds video content in a document.",
    "<wbr>": "Represents a line break opportunity for very long words or strings of text without spaces.",
    "<xmp>": "Deprecated. Was used to preformat text, preserving spaces and line breaks. Use <pre> instead.",

}

# Determine if the background is dark or light
def is_dark(rgb_tuple):
    return sum(rgb_tuple) / 3 < 128

# Function to calculate the maximum width a line of text can occupy
def max_text_width(font, image_width, padding):
    return image_width - (2 * padding)

# Generate images with the specifications
def generate_images(tags_dict, font_path, tag_font_size, desc_font_size, padding):
    tag_font = ImageFont.truetype(font_path, tag_font_size)
    desc_font = ImageFont.truetype(font_path, desc_font_size)
    
    for tag, description in tags_dict.items():
        try:
            color_name, rgb_tuple = random.choice(list(css_colors_rgb.items()))
            text_color = "white" if is_dark(rgb_tuple) else "black"

            image = Image.new("RGB", (width, height), color=rgb_tuple)
            draw = ImageDraw.Draw(image)

            # Calculate the maximum width for text based on padding
            max_width = max_text_width(desc_font, width, padding)
            # Adjust the wrapper width based on the maximum text width and font size
            wrapper = textwrap.TextWrapper(width=int(max_width / (desc_font_size * 0.6)))

            wrapped_description = wrapper.wrap(text=description)
            tag_width, tag_height = draw.textsize(tag, font=tag_font)
            desc_height = sum([draw.textsize(line, font=desc_font)[1] for line in wrapped_description])
            total_height = tag_height + desc_height + (10 * (len(wrapped_description) - 1))

            initial_y = (height - total_height) / 2
            tag_x = (width - tag_width) / 2
            draw.text((tag_x, initial_y), tag, fill=text_color, font=tag_font)

            current_y = initial_y + tag_height + 20
            for line in wrapped_description:
                line_width, line_height = draw.textsize(line, font=desc_font)
                line_x = (width - line_width) / 2
                draw.text((line_x, current_y), line, fill=text_color, font=desc_font)
                current_y += line_height + 10

            filename = f"{tag[1:-1]}.png".replace(">", "_").replace("<", "").replace("/", "_")
            image.save(filename)
            print(f"Image saved: {filename}")

           # Append text data to the text file
            text_file.write(f"Tag: {tag}\n")
            text_file.write(f"{description}\n\n")
        except:
            print("error")

    text_file.close()

generate_images(html_tags_dict, font_path, tag_font_size, desc_font_size, padding)
