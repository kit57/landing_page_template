ROLE_PROMPT = """You are a web development expert specializing in creating clean, modern, standalone HTML/CSS landing pages with no external dependencies."""

LANDING_CUSTOM_PAGE_TEMPLATE_PROMPT = """Generate complete HTML and CSS code for a modern, responsive landing page based on the following user description:
        "{user_input}"
        
        The landing page must include:
        - A header with a business name (inferred from the description or generic if unclear) and navigation (Home, Features, Contact)
        - A hero section with a headline, subheadline, and call-to-action button
        - A features section with at least 3 features
        - A footer with basic contact info and copyright
        - Responsive design using CSS (mobile-first approach)
        - Modern, clean styling with a color scheme inferred from the description (or a default blue scheme if not specified)
        - Inline CSS within a <style> tag in the HTML file
        - No external dependencies or frameworks
        - Valid HTML5 and CSS3 syntax
        
        Return only the complete HTML code with embedded CSS, ready to be saved as a single .html file."""

LANDING_GENERAL_PAGE_TEMPLATE_PROMPT = """Generate complete HTML and CSS code for a general-purpose, modern, responsive landing page. Assume a generic business or service (e.g., a tech startup or online store).
        
        The landing page must include:
        - A header with a generic business name (e.g., 'Your Business') and navigation (Home, Features, Contact)
        - A hero section with a headline, subheadline, and call-to-action button (e.g., 'Get Started')
        - A features section with at least 3 generic features
        - A footer with basic contact info and copyright
        - Responsive design using CSS (mobile-first approach)
        - Modern, clean styling with a default blue color scheme
        - Inline CSS within a <style> tag in the HTML file
        - No external dependencies or frameworks
        - Valid HTML5 and CSS3 syntax
        
        Return only the complete HTML code with embedded CSS, ready to be saved as a single .html file."""