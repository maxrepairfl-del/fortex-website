"""Inline SVG icons (stroke-based line icons, themeable via currentColor)."""

_PATHS = {
    # ---- appliances ----
    "refrigerator": '<rect x="6" y="2.5" width="12" height="19" rx="2.2"/><path d="M6 9.5h12"/><path d="M9 5.5v2"/><path d="M9 12v3"/>',
    "dishwasher": '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M4 8h16"/><path d="M7 5.5h2"/><path d="M11 5.5h6"/><path d="M8 11.5c1.5 2 4 2 4 4.5"/><path d="M14 11.5c-1.2 1.6 0 3 1.5 3.5"/>',
    "washer": '<rect x="4" y="2.5" width="16" height="19" rx="2"/><circle cx="12" cy="14" r="4.5"/><circle cx="12" cy="14" r="1.8"/><circle cx="7.5" cy="5.8" r="1"/><path d="M11 5.8h6"/>',
    "dryer": '<rect x="4" y="2.5" width="16" height="19" rx="2"/><circle cx="12" cy="14" r="4.5"/><path d="M9.5 12.5c1.2 1 3.8 1 5 2.5"/><circle cx="7.5" cy="5.8" r="1"/><circle cx="16.5" cy="5.8" r="1"/>',
    "freezer": '<rect x="6" y="2.5" width="12" height="19" rx="2.2"/><path d="M9 5.5h2"/><path d="M12 8.5v9M9.1 10.2l5.8 5.6M14.9 10.2l-5.8 5.6"/>',
    "disposal": '<path d="M7 3h10l-1 4H8z"/><path d="M8 7v4a4 4 0 0 0 8 0V7"/><path d="M9.5 14.5v3a2.5 2.5 0 0 0 5 0v-3"/>',
    "microwave": '<rect x="2.5" y="5" width="19" height="14" rx="2"/><rect x="5" y="8" width="9" height="8" rx="1"/><path d="M17 8.5v.01M17 11.5v.01M17 14.5h1"/>',
    "oven": '<rect x="4" y="3" width="16" height="18" rx="2"/><circle cx="8" cy="6.5" r="1"/><circle cx="12" cy="6.5" r="1"/><circle cx="16" cy="6.5" r="1"/><rect x="7" y="10.5" width="10" height="8" rx="1"/>',
    "vent": '<path d="M3 8h11a4 4 0 1 0-4-4"/><path d="M3 12h15a3 3 0 1 1-3 3"/><path d="M3 16h9a3.5 3.5 0 1 0-3.5 3.5"/>',
    "wine": '<path d="M8 3h8l-1 5a3 3 0 0 1-6 0z"/><path d="M12 13v6"/><path d="M8.5 21h7"/>',
    "commercial-freezer": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M12 3v18"/><path d="M7.5 8v3M16.5 8v3"/><path d="m9 14 1.5 1.5L9 17M15 14l-1.5 1.5L15 17"/>',
    "ice": '<rect x="3" y="8" width="9" height="9" rx="1.5"/><rect x="10" y="11" width="9" height="9" rx="1.5"/><path d="M14 4l1.2 2.5L18 7l-2 1.8.5 2.7L14 10l-2.5 1.5.5-2.7L10 7l2.8-.5z"/>',

    # ---- UI ----
    "phone": '<path d="M5 3.5h3l1.5 4-2 1.4a12 12 0 0 0 5.6 5.6l1.4-2 4 1.5v3a2 2 0 0 1-2.2 2A16.5 16.5 0 0 1 3 5.7 2 2 0 0 1 5 3.5z"/>',
    "calendar": '<rect x="3.5" y="5" width="17" height="15" rx="2"/><path d="M3.5 9.5h17M8 3v4M16 3v4"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7.5V12l3 2"/>',
    "shield": '<path d="M12 2.5 4.5 5.5v5c0 5 3.2 8.4 7.5 10 4.3-1.6 7.5-5 7.5-10v-5z"/><path d="m9 12 2 2 4-4"/>',
    "shield-plain": '<path d="M12 2.5 4.5 5.5v5c0 5 3.2 8.4 7.5 10 4.3-1.6 7.5-5 7.5-10v-5z"/>',
    "star": '<path d="m12 3 2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 17.8 6.8 19.2l1-5.8-4.3-4.1 5.9-.9z" fill="currentColor" stroke="none"/>',
    "arrow-right": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "pin": '<path d="M12 21s7-5.6 7-11a7 7 0 1 0-14 0c0 5.4 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/>',
    "check": '<path d="M5 12.5 10 17l9-10"/>',
    "check-circle": '<circle cx="12" cy="12" r="9"/><path d="m8 12 2.5 2.5L16 9"/>',
    "wrench": '<path d="M15.5 7.5a4 4 0 0 1-5.2 5.2L5 18l1 1 5.3-5.3a4 4 0 0 0 5.2-5.2l-2.3 2.3-2-2z"/>',
    "tools": '<path d="M6 3l3 3-2 2-3-3a3 3 0 0 0 4 4l8 8a2 2 0 0 0 3-3l-8-8"/><path d="m14 7 3-3 3 3-3 3"/>',
    "truck": '<path d="M2.5 6.5h11v9h-11z"/><path d="M13.5 9.5h4l3 3v3h-7z"/><circle cx="6.5" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/>',
    "award": '<circle cx="12" cy="9" r="5.5"/><path d="m9 14-1.5 7L12 19l4.5 2L15 14"/>',
    "tag": '<path d="M3 12.5 11.5 4H20v8.5L11.5 21z"/><circle cx="15.5" cy="8.5" r="1.4"/>',
    "bolt": '<path d="M13 2 4 13h6l-1 9 9-11h-6z" fill="currentColor" stroke="none"/>',
    "chat": '<path d="M4 5h16v11H9l-4 4V5z"/><path d="M8 9.5h8M8 12.5h5"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "close": '<path d="M6 6l12 12M18 6 6 18"/>',
    "thumb": '<path d="M7 10v10H4V10z"/><path d="M7 10l4-7a2 2 0 0 1 2 2v3h5a2 2 0 0 1 2 2.3l-1.2 6A2 2 0 0 1 16.8 20H7"/>',
    "sparkle": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4" /><path d="m6.5 6.5 2 2M15.5 15.5l2 2M17.5 6.5l-2 2M8.5 15.5l-2 2"/>',
    "dollar": '<circle cx="12" cy="12" r="9"/><path d="M14.5 9c-.5-1-1.5-1.5-2.7-1.5-1.5 0-2.6.8-2.6 2 0 3 5.6 1.5 5.6 4.5 0 1.3-1.2 2.1-2.7 2.1-1.4 0-2.5-.6-3-1.6M12 6v1.5M12 16.5V18"/>',
    "heart": '<path d="M12 20s-7-4.5-7-9.5A3.5 3.5 0 0 1 12 7a3.5 3.5 0 0 1 7 3.5C19 15.5 12 20 12 20z"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 20c0-4 3.5-6 8-6s8 2 8 6"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.5 6.5 8.5 6 8.5-6"/>',
    "leaf": '<path d="M4 20c0-9 7-15 16-15 0 9-6 15-15 15"/><path d="M4 20c4-6 8-8 12-9"/>',
    "play": '<circle cx="12" cy="12" r="9"/><path d="m10 8.5 6 3.5-6 3.5z" fill="currentColor" stroke="none"/>',
}


def icon(name, cls="", size=24, stroke=1.8):
    inner = _PATHS.get(name, "")
    c = f' class="{cls}"' if cls else ""
    return (
        f'<svg{c} viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" '
        f'stroke="currentColor" stroke-width="{stroke}" stroke-linecap="round" '
        f'stroke-linejoin="round" aria-hidden="true">{inner}</svg>'
    )


def logo_mark(cls="mark"):
    """Fortex shield mark — appliance + circuit motif, single color (currentColor)."""
    return f'''<svg class="{cls}" viewBox="0 0 48 56" fill="none" aria-hidden="true">
  <path d="M24 2.5 43 9.2c1.3.5 1.8 1.2 1.8 2.6v17.4c0 12.9-9 20-20.8 24.3C12.2 49.2 3.2 42.1 3.2 29.2V11.8c0-1.4.5-2.1 1.8-2.6z"
        stroke="currentColor" stroke-width="2.6" stroke-linejoin="round"/>
  <rect x="14.5" y="14" width="19" height="15" rx="2.2" stroke="currentColor" stroke-width="2.2"/>
  <circle cx="18.5" cy="17.6" r="1.15" fill="currentColor"/>
  <circle cx="23" cy="17.6" r="1.15" fill="currentColor"/>
  <circle cx="27.5" cy="17.6" r="1.15" fill="currentColor"/>
  <path d="M19 33v4.5M24 33v7M29 33v4.5M19 37.5h10" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
  <circle cx="19" cy="39.5" r="1.9" fill="currentColor"/>
  <circle cx="29" cy="39.5" r="1.9" fill="currentColor"/>
  <circle cx="24" cy="42.2" r="1.9" fill="currentColor"/>
</svg>'''
