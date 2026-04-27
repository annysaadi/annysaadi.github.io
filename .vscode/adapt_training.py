import re

def adapt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Images: Add lazy loading and async decoding where missing.
    # Fix regex to place the attributes right before the closing > or />
    def adapt_imgs(match):
        img_content = match.group(1)
        closing = match.group(2)
        if 'loading=' not in img_content:
            return f'{img_content} loading="lazy" decoding="async"{closing}'
        return match.group(0)

    html = re.sub(r'(<img\b[^>]*?)\s*(/?>)', adapt_imgs, html)

    # 2. Iframes: Add lazy loading where missing
    def adapt_iframes(match):
        iframe_content = match.group(1)
        closing = match.group(2)
        if 'loading=' not in iframe_content:
            return f'{iframe_content} loading="lazy"{closing}'
        return match.group(0)

    html = re.sub(r'(<iframe\b[^>]*?)\s*(/?>)', adapt_iframes, html)

    # 3. Add text-wrap balance to CSS if not present
    if "/* Impeccable Adapt" not in html:
        css_injection = """
  <style>
    /* Impeccable Adapt - Responsive Typography & Layout */
    h1, h2, h3, .hero-title, .sec-title, .final-title {
      text-wrap: balance;
    }
    p, .sec-body, .final-sub, .call-desc {
      text-wrap: pretty;
    }
    /* Make hardcoded breaks responsive */
    @media (max-width: 768px) {
      .r-br { display: none; }
    }
  </style>
</head>"""
        html = html.replace("</head>", css_injection)

    # 4. Replace hardcoded <br> in titles with responsive <br>
    def adapt_header_brs(match):
        inner = match.group(2)
        # Replaces all variations of <br> with <br class="r-br"/>
        inner_replaced = re.sub(r'<br\s*/?>', r'<br class="r-br"/>', inner)
        return match.group(1) + inner_replaced + match.group(3)

    html = re.sub(r'(<(h[1-6])[^>]*>)(.*?)(</\2>)', adapt_header_brs, html, flags=re.DOTALL)

    # 5. External links: ensure target="_blank" and rel="noopener noreferrer"
    def adapt_external_links(match):
        tag = match.group(0)
        if 'target="_blank"' not in tag:
            tag = tag.replace('href="http', 'target="_blank" rel="noopener noreferrer" href="http')
        elif 'rel=' not in tag:
            tag = tag.replace('target="_blank"', 'target="_blank" rel="noopener noreferrer"')
        return tag

    html = re.sub(r'<a\b[^>]*href="https?[^>]+>', adapt_external_links, html)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    adapt("c:/Users/loany/Documents/annysaadi.github.io/annysaadi.github.io/.vscode/training_work.html")
