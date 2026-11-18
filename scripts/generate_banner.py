from datetime import datetime, timedelta, timezone

IST = timezone(timedelta(hours=5, minutes=30))
now = datetime.now(IST)
hour = now.hour
time_str = now.strftime("%I:%M %p IST").lstrip("0")

if 5 <= hour < 12:
    theme = {
        "phase": "MORNING",
        "sky_top": "#172554",
        "sky_bot": "#38BDF8",
        "city_a": "#1E3A5F",
        "city_b": "#254B7A",
        "stars_opacity": "0",
        "city_lit": "0.15",
        "accent": "#FBBF24",
        "celestial": """
  <!-- Rising Morning Sun -->
  <rect x="208" y="64" width="24" height="24" fill="#FDE047" />
  <rect x="204" y="68" width="32" height="16" fill="#FDE047" />
  <rect x="212" y="60" width="16" height="32" fill="#FEF08A" opacity="0.45" />
""",
    }
elif 12 <= hour < 17:
    theme = {
        "phase": "AFTERNOON",
        "sky_top": "#0369A1",
        "sky_bot": "#7DD3FC",
        "city_a": "#1E3A5F",
        "city_b": "#294D7A",
        "stars_opacity": "0",
        "city_lit": "0.05",
        "accent": "#38BDF8",
        "celestial": """
  <!-- Bright Afternoon Sun + Pixel Cloud -->
  <rect x="218" y="42" width="20" height="20" fill="#FEF08A" />
  <rect x="74" y="54" width="38" height="10" fill="#E0F2FE" opacity="0.85" />
  <rect x="82" y="48" width="22" height="6" fill="#F0F9FF" opacity="0.9" />
  <rect x="150" y="64" width="34" height="8" fill="#E0F2FE" opacity="0.75" />
""",
    }
elif 17 <= hour < 20:
    theme = {
        "phase": "EVENING",
        "sky_top": "#3B0764",
        "sky_bot": "#F97316",
        "city_a": "#1E1B3A",
        "city_b": "#2B224A",
        "stars_opacity": "0.35",
        "city_lit": "0.65",
        "accent": "#FB923C",
        "celestial": """
  <!-- Sunset Horizon Sun -->
  <rect x="198" y="78" width="28" height="20" fill="#FB923C" />
  <rect x="202" y="74" width="20" height="24" fill="#FDBA74" opacity="0.85" />
""",
    }
else:
    theme = {
        "phase": "NIGHT",
        "sky_top": "#060914",
        "sky_bot": "#0B1328",
        "city_a": "#0F172A",
        "city_b": "#15223D",
        "stars_opacity": "1",
        "city_lit": "0.8",
        "accent": "#A3E635",
        "celestial": """
  <!-- Crescent Moon -->
  <rect x="220" y="44" width="16" height="16" fill="#FDE68A" />
  <rect x="226" y="44" width="12" height="12" fill="#060914" />
""",
    }

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 240" width="900" height="240" shape-rendering="crispEdges">
  <defs>
    <linearGradient id="skyGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{theme['sky_top']}" />
      <stop offset="100%" stop-color="{theme['sky_bot']}" />
    </linearGradient>
  </defs>
  <style>
    @keyframes blink {{
      0%, 49% {{ opacity: 1; }}
      50%, 100% {{ opacity: 0.15; }}
    }}
    @keyframes twinkle {{
      0%, 100% {{ opacity: 0.25; }}
      50% {{ opacity: 0.95; }}
    }}
    @keyframes steam1 {{
      0% {{ transform: translateY(0px); opacity: 0.85; }}
      100% {{ transform: translateY(-14px); opacity: 0; }}
    }}
    @keyframes steam2 {{
      0% {{ transform: translateY(0px); opacity: 0.65; }}
      100% {{ transform: translateY(-18px); opacity: 0; }}
    }}
    @keyframes typeBob {{
      0%, 100% {{ transform: translateY(0px); }}
      50% {{ transform: translateY(2px); }}
    }}
    @keyframes pulseBar {{
      0%, 100% {{ opacity: 0.45; }}
      50% {{ opacity: 1; }}
    }}
    .cursor {{ animation: blink 1s steps(1) infinite; }}
    .star-a {{ animation: twinkle 2.8s ease-in-out infinite; }}
    .star-b {{ animation: twinkle 3.6s ease-in-out 1.1s infinite; }}
    .star-c {{ animation: twinkle 4.2s ease-in-out 0.5s infinite; }}
    .steam-a {{ animation: steam1 2.4s ease-out infinite; }}
    .steam-b {{ animation: steam2 2.4s ease-out 1.1s infinite; }}
    .hands {{ animation: typeBob 0.55s steps(2) infinite; }}
    .head {{ animation: typeBob 2.2s steps(2) infinite; }}
    .led-1 {{ animation: blink 1.6s steps(1) infinite; }}
    .led-2 {{ animation: blink 2.3s steps(1) 0.7s infinite; }}
    .wave {{ animation: pulseBar 2s ease-in-out infinite; }}
  </style>

  <!-- Room Backdrop -->
  <rect width="900" height="240" fill="#090A0E" />
  <rect x="0" y="180" width="900" height="60" fill="#0D0F14" />
  <rect x="0" y="178" width="900" height="4" fill="#181B24" />

  <!-- Window Frame -->
  <rect x="44" y="24" width="236" height="132" fill="#1A1E2B" />
  <rect x="52" y="32" width="220" height="116" fill="url(#skyGrad)" />

  <!-- Stars (visible Evening/Night) -->
  <g opacity="{theme['stars_opacity']}">
    <rect x="74" y="48" width="4" height="4" fill="#E2E8F0" class="star-a" />
    <rect x="116" y="64" width="4" height="4" fill="#93C5FD" class="star-b" />
    <rect x="152" y="42" width="4" height="4" fill="#E2E8F0" class="star-c" />
    <rect x="198" y="72" width="4" height="4" fill="#A3E635" class="star-a" />
    <rect x="242" y="50" width="4" height="4" fill="#E2E8F0" class="star-b" />
    <rect x="92" y="92" width="4" height="4" fill="#CBD5E1" class="star-c" />
  </g>
{theme['celestial']}
  <!-- Distant Pune Skyline -->
  <rect x="52" y="114" width="28" height="34" fill="{theme['city_a']}" />
  <rect x="80" y="102" width="32" height="46" fill="{theme['city_b']}" />
  <rect x="112" y="120" width="24" height="28" fill="{theme['city_a']}" />
  <rect x="136" y="96" width="38" height="52" fill="{theme['city_b']}" />
  <rect x="174" y="112" width="34" height="36" fill="{theme['city_a']}" />
  <rect x="208" y="106" width="32" height="42" fill="{theme['city_b']}" />
  <rect x="240" y="118" width="32" height="30" fill="{theme['city_a']}" />

  <!-- City Windows -->
  <g opacity="{theme['city_lit']}">
    <rect x="88" y="110" width="4" height="4" fill="#FACC15" />
    <rect x="148" y="106" width="4" height="4" fill="#60A5FA" />
    <rect x="156" y="118" width="4" height="4" fill="#FACC15" />
    <rect x="218" y="114" width="4" height="4" fill="#60A5FA" />
  </g>

  <!-- Window Crossbar -->
  <rect x="160" y="32" width="4" height="116" fill="#1A1E2B" />
  <rect x="52" y="92" width="220" height="4" fill="#1A1E2B" />

  <!-- Top-Right Pixel Lab Card (Shorter 21Y · AI / ML + Live Time Phase) -->
  <rect x="612" y="22" width="248" height="60" fill="#10131A" />
  <rect x="612" y="22" width="248" height="2" fill="#27272A" />
  <rect x="612" y="80" width="248" height="2" fill="#27272A" />
  <rect x="612" y="22" width="2" height="60" fill="#27272A" />
  <rect x="858" y="22" width="2" height="60" fill="#27272A" />
  <rect x="624" y="34" width="6" height="6" fill="{theme['accent']}" class="led-1" />
  <text x="638" y="41" fill="#F2F2F2" font-family="monospace" font-size="12" font-weight="bold">PUSHKAR_AI_LAB</text>
  <text x="624" y="57" fill="#A1A1AA" font-family="monospace" font-size="10">21Y · AI / ML</text>
  <text x="624" y="72" fill="{theme['accent']}" font-family="monospace" font-size="10">{theme['phase']} · {time_str}</text>

  <!-- Desk Surface -->
  <rect x="290" y="176" width="560" height="10" fill="#222633" />
  <rect x="304" y="186" width="532" height="54" fill="#141720" />
  <rect x="318" y="186" width="10" height="54" fill="#0B0D12" />
  <rect x="812" y="186" width="10" height="54" fill="#0B0D12" />

  <!-- Local LLM Tower -->
  <rect x="752" y="112" width="54" height="64" fill="#1A1D26" />
  <rect x="756" y="116" width="46" height="56" fill="#101218" />
  <rect x="764" y="124" width="6" height="4" fill="{theme['accent']}" class="led-1" />
  <rect x="774" y="124" width="6" height="4" fill="#60A5FA" class="led-2" />
  <rect x="784" y="124" width="6" height="4" fill="#A78BFA" class="led-1" />
  <rect x="764" y="138" width="30" height="4" fill="#1F2430" />
  <rect x="764" y="146" width="30" height="4" fill="#1F2430" />
  <rect x="764" y="154" width="30" height="4" fill="#1F2430" />
  <rect x="764" y="162" width="30" height="4" fill="#1F2430" />

  <!-- Main Monitor -->
  <rect x="468" y="76" width="176" height="84" fill="#242938" />
  <rect x="474" y="82" width="164" height="72" fill="#070B12" />
  <rect x="546" y="160" width="20" height="12" fill="#242938" />
  <rect x="530" y="170" width="52" height="6" fill="#2D3345" />
  <rect x="480" y="174" width="152" height="2" fill="{theme['accent']}" opacity="0.35" />

  <!-- Screen Content -->
  <rect x="482" y="90" width="68" height="4" fill="{theme['accent']}" />
  <rect x="482" y="100" width="52" height="4" fill="#60A5FA" />
  <rect x="482" y="108" width="60" height="4" fill="#94A3B8" />
  <rect x="482" y="116" width="44" height="4" fill="#A78BFA" />
  <rect x="482" y="124" width="58" height="4" fill="#64748B" />
  <rect x="482" y="134" width="32" height="4" fill="{theme['accent']}" />
  <rect x="518" y="134" width="6" height="6" fill="{theme['accent']}" class="cursor" />

  <rect x="560" y="88" width="2" height="60" fill="#1E293B" />

  <rect x="570" y="92" width="58" height="4" fill="#38BDF8" opacity="0.7" />
  <rect x="572" y="122" width="6" height="16" fill="#60A5FA" class="wave" />
  <rect x="582" y="110" width="6" height="28" fill="{theme['accent']}" class="wave" />
  <rect x="592" y="116" width="6" height="22" fill="#A78BFA" class="wave" />
  <rect x="602" y="104" width="6" height="34" fill="{theme['accent']}" class="wave" />
  <rect x="612" y="118" width="6" height="20" fill="#60A5FA" class="wave" />
  <rect x="622" y="126" width="6" height="12" fill="#38BDF8" class="wave" />

  <!-- Side Laptop -->
  <rect x="372" y="126" width="64" height="42" fill="#202431" />
  <rect x="376" y="130" width="56" height="34" fill="#0A0E17" />
  <rect x="366" y="168" width="76" height="8" fill="#2D3345" />
  <rect x="382" y="136" width="36" height="4" fill="#60A5FA" />
  <rect x="382" y="144" width="44" height="4" fill="#475569" />
  <rect x="382" y="152" width="28" height="4" fill="{theme['accent']}" />

  <!-- Steaming Coffee Mug -->
  <rect x="684" y="156" width="18" height="20" fill="#E5E7EB" />
  <rect x="702" y="160" width="6" height="10" fill="#CBD5E1" />
  <rect x="686" y="156" width="14" height="4" fill="#78350F" />
  <rect x="688" y="144" width="4" height="6" fill="#94A3B8" class="steam-a" />
  <rect x="694" y="140" width="4" height="6" fill="#CBD5E1" class="steam-b" />

  <!-- Developer Seated & Coding -->
  <rect x="524" y="146" width="60" height="58" fill="#181A22" />
  <rect x="548" y="204" width="12" height="36" fill="#252834" />
  <rect x="528" y="132" width="52" height="44" fill="#111318" />
  <rect x="534" y="136" width="40" height="36" fill="#171920" />
  <g class="hands">
    <rect x="520" y="164" width="16" height="10" fill="#C68B59" />
    <rect x="572" y="164" width="16" height="10" fill="#C68B59" />
  </g>
  <g class="head">
    <rect x="536" y="96" width="36" height="36" fill="#18161B" />
    <rect x="534" y="102" width="40" height="24" fill="#18161B" />
    <rect x="544" y="128" width="20" height="6" fill="#C68B59" />
    <rect x="540" y="94" width="28" height="4" fill="#27252C" />
  </g>

  <!-- Subtle Bottom Accent Line -->
  <rect x="0" y="236" width="900" height="4" fill="{theme['accent']}" opacity="0.3" />
</svg>
"""

with open("banner.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print(f"Updated banner.svg for {theme['phase']} ({time_str})")

import re

ts = now.strftime("%Y%m%d%H%M")
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

fresh_url = f"https://raw.githubusercontent.com/PushkarEz/PushkarEz/main/banner.svg?v={ts}"
readme = re.sub(
    r'(\./banner\.svg(?:\?v=\d+)?|https://raw\.githubusercontent\.com/PushkarEz/PushkarEz/main/banner\.svg(?:\?v=\d+)?)',
    fresh_url,
    readme,
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)
