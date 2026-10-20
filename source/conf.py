# Configuration file for the Sphinx documentation builder.
# Daz Studio 4.x Documentation — Khmer Edition (Read the Docs design)

project = "Daz Studio 4.x"
copyright = "មាតិកាដើម © DAZ 3D, LP (CC BY 3.0) · ការបកប្រែខ្មែរ © សហគមន៍ (CC BY 4.0)"
author = "SeyhaLite"

language = "km"

extensions = ["sphinx_sitemap"]

templates_path = ["_templates"]
html_static_path = ["_static"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Read the Docs theme (ដូច docs.godotengine.org / readthedocs.com) ---------
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "collapse_navigation": True,         # ស្តង់ដារ RTD — ពង្រីកស្វ័យប្រវត្តិតែទំព័របច្ចុប្បន្ន
    "sticky_navigation": True,
    "navigation_depth": 2,
    "includehidden": True,
    "titles_only": False,
    "prev_next_buttons_location": "bottom",
    "style_external_links": True,
    "flyout_display": "hidden",
    "vcs_pageview_mode": "edit",         # "Edit on GitHub" បើកទៅ form កែផ្ទាល់
}

html_logo = "_static/daz-logo.png"
html_favicon = "_static/daz-logo.png"

# sidebar header: light strip so the real DAZ logo reads clearly
html_theme_options["style_nav_header_background"] = "#1f2328"

# Edit on GitHub button ( breadcrumb ខាងស្ដាំ )
html_context = {
    "display_github": True,
    "github_user": "SeyhaLite",
    "github_repo": "daz3d-khmer-docs",
    "github_version": "main",
    "conf_py_path": "/source/",
}

html_title = "Daz Studio 4.x ឯកសារខ្មែរ"
html_short_title = "Daz Studio 4.x"
html_show_sphinx = False
html_copy_source = False
html_last_updated_fmt = "%d %b %Y"
html_search_language = "en"

# Khmer fonts + dark mode (custom, minimal — RTD design preserved)
html_css_files = ["khmer.css"]  # Sphinx auto-appends content hash (cache-bust)

# -- SEO ---------------------------------------------------------------------
html_baseurl = "https://seyhalite.github.io/daz3d-khmer-docs/"   # sitemap.xml + canonical
html_extra_path = ["_extra"]                                      # robots.txt
sitemap_url_scheme = "{link}"                                  # baseurl + page path
