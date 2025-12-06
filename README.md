# Vinelife Wilmslow

A modern, responsive church website for Vinelife Wilmslow - a community church in the heart of Wilmslow, Cheshire, UK.

<img width="1800" height="1062" alt="Vinelife Wilmslow Website Screenshot" src="https://github.com/user-attachments/assets/d85431cc-739b-4e92-be67-1de14de8610b" />

## 🌟 Features

### 📱 Responsive Design
- Fully responsive design that works on desktop, tablet, and mobile devices
- Modern CSS Grid and Flexbox layout
- Bootstrap 5 integration for consistent styling

### 🎨 Visual Design
- **Grape-inspired color palette** with deep purples, greens, and complementary corals
- **Elegant typography** using Crimson Text for headings and Open Sans for body text
- **Parallax backgrounds** with gradient overlays for visual depth
- **Smooth animations** and hover effects throughout

### 📄 Website Sections

#### 🏠 Hero Section
- Welcome message with church mission
- Call-to-action buttons
- Social media links (Facebook & YouTube)
- Stunning background imagery

#### ℹ️ About Section
- Comprehensive church history since 2000
- Information about church planting and training
- Community involvement and outreach programs
- Details about Hope Central charity partnership

#### 👥 Leaders Section
- Meet Robert & Cheryl Larkman
- Leadership background and vision
- Professional photography
- Personal story and community connection

#### ⛪ Services Section
- Sunday worship times (10:30 AM most Sundays)
- Service location at The Open Arms Youth Project
- Easy-to-find service information

#### 📅 Events Section
- Monthly event calendar with interactive cards
- Event types: Coffee & Chat, Worship Meetings, Summer Recess
- Location and timing details
- Visual event categorization with icons

#### 🎬 **NEW! YouTube Channel Section**
- **Dedicated YouTube section** with channel branding
- **Direct links** to https://www.youtube.com/@vinelifewilmslow5572
- **Feature highlights**: Live Services, Sermons, Events
- **Subscribe button** for easy channel subscription
- **Animated YouTube icon** with pulse effect

#### 🔗 Resources Section
- **CAP (Christians Against Poverty)** - Debt support services
- **Alpha Course** - Faith exploration program
- **Hope Central** - Local charity for food banks and community support
- External links to partner organizations

#### 📍 Find Us Section
- **Interactive Google Maps** embed
- **Complete address**: The Open Arms Youth Project, Howty Close, Wilmslow SK9 2SH
- **Service times** and parking information
- **Contact details** in an accessible format

#### 📧 Contact Section
- **Contact form** with validation
- **Required fields**: Name, phone number, message
- **Optional email** field with validation
- **Form submission** with user feedback
- **Social media links** (Facebook & YouTube)

### 🛠️ Technical Features

#### 🎯 Performance Optimizations
- **WebP image format** for faster loading
- **Lazy loading** for images
- **Preloaded critical fonts**
- **Compressed assets** and optimized code

#### ♿ Accessibility
- **ARIA labels** for screen readers
- **Semantic HTML** structure
- **Focus management** for keyboard navigation
- **Color contrast** compliance

#### 📱 Mobile-First Design
- **Collapsible navigation** for mobile devices
- **Touch-friendly buttons** and interactive elements
- **Responsive image sizing**
- **Optimized mobile typography**

#### 🔍 SEO Optimized
- **Meta descriptions** and proper title tags
- **Structured HTML** with semantic elements
- **Fast loading times**
- **Mobile-friendly design**

## 🚀 Running the Website Locally

### Method 1: Python HTTP Server (Recommended)
```bash
cd vinelifewilmslow
python3 -m http.server 8000
```
Then visit: http://localhost:8000

### Method 2: Using npx serve
```bash
cd vinelifewilmslow
npx serve -s . -l 5000
```
Then visit: http://localhost:5000

### Method 3: VS Code Live Server
- Install the "Live Server" extension in VS Code
- Right-click `index.html` and select "Open with Live Server"

## 🗂️ Project Structure

```
vinelifewilmslow/
├── index.html                 # Main website file
├── README.md                  # This documentation
├── assets/
│   ├── css/
│   │   └── style.css         # Custom stylesheet with grape color palette
│   ├── favicons/             # Website icons
│   └── images/               # Optimized WebP images
│       ├── vinelifewilmslowlogo.webp
│       ├── vinelifechurch.webp
│       ├── Vinelife.webp
│       ├── 2305+R-C-1920w.webp
│       ├── worship.webp
│       ├── Vineyardchurch.webp
│       ├── resources.webp
│       ├── bokeh.webp
│       ├── bokeh1.webp
│       ├── caplogo.webp
│       ├── alphalogo.webp
│       └── hopecentral.webp
```

## 🎨 Design System

### Color Palette
- **Primary**: Deep purple grapes (#320322, #4a0e4e)
- **Secondary**: Forest and emerald greens (#2d4a22, #4a6741)
- **Accent**: Coral and orange (#ff6b47, #ff7043)
- **Background**: Cream and charcoal (#faf7f0, #2e2e2e)

### Typography
- **Headings**: Crimson Text (serif, elegant)
- **Body**: Open Sans (sans-serif, readable)

### Components
- **Gradient backgrounds** with parallax effects
- **Card-based layouts** for events and resources
- **Interactive buttons** with hover animations
- **Social media integration**

## 🔗 External Integrations

- **Google Fonts** (Crimson Text & Open Sans)
- **Font Awesome** icons
- **Bootstrap 5** CSS framework
- **Google Maps** embed
- **Facebook** page integration
- **YouTube** channel integration

## 🌐 Social Media Links

- **Facebook**: [VinelifeChurchWilmslow](https://www.facebook.com/VinelifeChurchWilmslow)
- **YouTube**: [@vinelifewilmslow5572](https://www.youtube.com/@vinelifewilmslow5572)

## 📋 Recent Updates

### November 2025
- ✅ Added dedicated YouTube channel section
- ✅ Updated all YouTube links to new channel URL
- ✅ Enhanced responsive design
- ✅ Improved accessibility features
- ✅ Optimized performance with WebP images

## � Future Development Possibilities

### 🐍 Django Content Management System

The current static website could be enhanced with a Django-powered backend to enable dynamic content management. This would allow church administrators to easily update content without technical knowledge.

#### Potential Benefits:
- **Admin Interface**: User-friendly Django admin for content updates
- **Dynamic Content**: Real-time updates without code changes
- **User Management**: Different permission levels for content editors
- **Database Storage**: Structured data management for events, sermons, etc.
- **Image Management**: Upload and organize media files
- **Form Handling**: Advanced contact and event registration forms

#### Proposed Architecture:

```
vinelife-cms/
├── src/
│   ├── manage.py
│   ├── vinelife_cms/
│   │   ├── settings/
│   │   │   ├── base.py
│   │   │   ├── development.py
│   │   │   └── production.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── apps/
│   │   ├── core/          # Homepage and navigation
│   │   ├── about/         # About section management
│   │   ├── leaders/       # Leadership profiles
│   │   ├── services/      # Service information
│   │   ├── events/        # Event calendar and management
│   │   ├── youtube/       # YouTube integration
│   │   ├── resources/     # Resource links management
│   │   └── contact/       # Contact forms and info
│   ├── templates/         # HTML templates
│   ├── static/           # CSS, JS, images
│   └── media/            # User uploads
├── requirements/
│   ├── base.txt
│   ├── development.txt
│   └── production.txt
└── README.md
```

#### Features to Implement:

##### 📝 **Content Management**
- **About Section**: Edit church history, mission, and values
- **Leadership**: Add/edit leader profiles with photos and bios
- **Services**: Update service times, locations, and descriptions
- **Events**: Create, edit, and delete events with rich text descriptions
- **YouTube**: Manage channel links and featured videos
- **Resources**: Add/remove resource links and descriptions

##### 📅 **Event Management**
- **Calendar Integration**: Monthly event calendar with categories
- **Event Types**: Different event categories (worship, coffee chat, etc.)
- **RSVP System**: Allow visitors to register for events
- **Event Images**: Upload and manage event photos

##### 📧 **Communication**
- **Contact Forms**: Enhanced contact form with email notifications
- **Newsletter Signup**: Email list management
- **Announcement System**: Display important announcements

##### 🎬 **Media Management**
- **YouTube Integration**: Embed latest videos automatically
- **Photo Gallery**: Upload and organize church photos
- **Sermon Archive**: Categorized sermon library

##### 👥 **User Management**
- **Admin Users**: Church staff with full editing permissions
- **Content Editors**: Volunteers with limited editing access
- **Viewer Analytics**: Track website engagement

#### Implementation Considerations:

##### 🚀 **Deployment Options**
- **Heroku**: Easy deployment with PostgreSQL
- **DigitalOcean**: VPS hosting for more control
- **PythonAnywhere**: Simple Python hosting solution
- **AWS/GCP**: Scalable cloud solutions

##### 🔒 **Security Features**
- **SSL Certificates**: Secure admin access
- **User Authentication**: Django's built-in auth system
- **CSRF Protection**: Form security
- **Input Validation**: Prevent malicious content

##### 📱 **Mobile Optimization**
- **Responsive Admin**: Mobile-friendly content editing
- **Touch-Friendly**: Easy content updates on tablets
- **Offline Capability**: PWA features for better UX

#### Migration Strategy:
1. **Phase 1**: Convert static content to Django templates
2. **Phase 2**: Create admin interface for content management
3. **Phase 3**: Add dynamic features (events, forms)
4. **Phase 4**: Implement advanced features (user accounts, analytics)

#### Technical Stack:
- **Backend**: Django 4.2+ with Python 3.9+
- **Database**: PostgreSQL (production) / SQLite (development)
- **Frontend**: Bootstrap 5 + existing CSS/JS
- **Media Storage**: AWS S3 or local file storage
- **Deployment**: Docker containers for consistency

> **Note**: The current static website would remain fully functional during development, allowing for gradual migration to the Django-powered version.

## �👥 About Vinelife Wilmslow

Vinelife Church Wilmslow was founded in 2000 as an evangelical and charismatic church providing culturally accessible expression of faith for unchurched people. Led by Robert & Cheryl Larkman, the church is actively involved in community outreach through partnerships with organizations like Hope Central, Christians Against Poverty, and Churches Together in Handforth.

**Service Times**: Sunday Worship at 10:30 AM (most Sundays)  
**Location**: The Open Arms Youth Project, Howty Close, Wilmslow SK9 2SH  
**Contact**: Available through the website contact form

---

*Built with ❤️ for the Vinelife Wilmslow community*
