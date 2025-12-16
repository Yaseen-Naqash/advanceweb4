from django.core.management.base import BaseCommand
from base.models import ProductFeature, Product
import random
from django.utils.text import slugify

class Command(BaseCommand):
    def handle(self, *args, **options):


        # Random clothing titles with different styles and categories
        clothing_titles = [
            "Classic Cotton T-Shirt", "Premium Oxford Shirt", "Slim Fit Jeans", "Cozy Hooded Sweatshirt",
            "Wool Blend Blazer", "Summer Linen Pants", "Stretch Denim Jacket", "Cashmere Sweater",
            "Athletic Performance Shorts", "Leather Biker Jacket", "Silk Evening Dress", "Cargo Work Pants",
            "Fleece Lined Jacket", "Corduroy Overshirt", "Ribbed Knit Top", "Wide Leg Trousers",
            "Puffer Winter Coat", "Polo Collar Shirt", "Crewneck Jumper", "Tailored Suit Trousers",
            "Bomber Flight Jacket", "Flannel Button Down", "Yoga Leggings", "Denim Overalls",
            "Trench Raincoat", "Knit Cardigan", "Chino Shorts", "Velvet Blazer",
            "Athletic Tank Top", "Cable Knit Sweater", "Cargo Shorts", "Satin Slip Dress",
            "Utility Vest", "French Terry Sweatshirt", "Leather Leggings", "Seersucker Suit",
            "Swim Trunks", "Wrap Maxi Dress", "Quilted Vest", "Jersey Tracksuit",
            "Evening Gown", "Military Field Jacket", "Corduroy Pants", "Cashmere Scarf",
            "Baseball Tee", "Parka Winter Jacket", "Pleated Skirt", "Linen Blouse",
            "Mesh Sport Top", "Denim Skirt", "Faux Fur Coat", "Turtleneck Sweater",
            "Cargo Joggers", "Silk Camisole", "Utility Jumpsuit", "Wool Peacoat",
            "Graphic Tee", "Suede Jacket", "Chiffon Blouse", "Thermal Underwear",
            "Basketball Shorts", "Evening Cape", "Work Coveralls", "Swim Cover-up",
            "Romper Jumpsuit", "Nehru Jacket", "Cropped Hoodie", "Palazzo Pants",
            "Sherpa Jacket", "Sequined Top", "Sweatpants", "Kimono Robe",
            "Blazer Dress", "Windbreaker", "Leg Warmers", "Smock Dress"
        ]

        # Random descriptions for clothing items
        clothing_descriptions = [
            "A versatile essential crafted from premium materials for everyday comfort and style.",
            "Experience ultimate comfort with this breathable fabric that moves with you throughout the day.",
            "Expertly tailored for a perfect fit, featuring thoughtful details and durable construction.",
            "Designed for both style and functionality, this piece transitions seamlessly from day to night.",
            "Made with sustainable materials and ethical production practices for conscious fashion.",
            "This wardrobe staple combines timeless design with modern performance features.",
            "Luxurious softness meets practical durability in this carefully crafted garment.",
            "Engineered for active lifestyles with moisture-wicking technology and flexible movement.",
            "Elegant simplicity with clean lines and premium finishing touches for sophisticated style.",
            "Rugged construction meets refined aesthetics for lasting wear and versatile pairing.",
            "Featuring innovative fabric technology that regulates temperature for all-season comfort.",
            "Artisanal details and unique textures create a distinctive statement piece.",
            "Minimalist design with maximum impact, perfect for building a capsule wardrobe.",
            "Contemporary cut with retro-inspired elements for fashion-forward appeal.",
            "Lightweight layers that provide warmth without bulk for transitional weather.",
            "Statement-making silhouette with dramatic details and luxurious fabrications.",
            "Easy-care properties make this an ideal choice for busy modern lifestyles.",
            "Classic heritage design updated with contemporary fits and sustainable materials.",
            "Versatile layering piece that adds texture and dimension to any outfit.",
            "Performance-oriented design with technical features for specialized activities.",
            "Bohemian-inspired details with free-flowing silhouettes and natural textures.",
            "Sharp tailoring and structured shapes create powerful professional presence.",
            "Cozy loungewear that doesn't compromise on style for relaxed days at home.",
            "Festival-ready vibes with playful prints and comfortable, moveable fabrics.",
            "Investment piece crafted to last with timeless appeal and superior quality.",
            "Gender-neutral design with adjustable features for personalized fit and style.",
            "Vintage-inspired craftsmanship meets modern sustainable production methods.",
            "Architectural lines and innovative draping create sculptural fashion statements.",
            "Packable and travel-friendly design that resists wrinkles for life on the go.",
            "Limited edition release featuring exclusive prints and special design details.",
            "Adaptive design with adjustable elements for customized comfort throughout the day.",
            "Artistic expression through unique fabric treatments and experimental silhouettes.",
            "Heritage brand authenticity with time-tested designs and premium materials.",
            "Modern workwear with functional pockets and durable reinforcements where needed.",
            "Romantic detailing with delicate fabrics and feminine silhouettes for special occasions.",
            "Urban streetwear edge with bold graphics and oversized proportions.",
            "Technical performance features hidden within stylish, everyday aesthetics.",
            "Seasonless design that works year-round with strategic layering options.",
            "Hand-finished details and artisanal techniques for truly unique pieces.",
            "Inclusive sizing with thoughtful design adjustments for different body types.",
            "Reversible design offers two looks in one for maximum versatility.",
            "Eco-conscious production using recycled materials and low-impact dyes.",
            "Therapeutic compression elements provide support during active movements.",
            "Adjustable features allow for personalized fit and style customization.",
            "Convertible design transforms for multiple wearing options and occasions.",
            "Smart fabric technology with responsive properties that adapt to conditions.",
            "Modest fashion with covered designs that maintain contemporary style.",
            "Athleisure aesthetic that blends workout functionality with casual comfort.",
            "Luxury craftsmanship with attention to every stitch and finishing detail.",
            "Collaboration edition featuring unique design elements from special partners.",
            "Weather-ready construction with protective elements for challenging conditions.",
            "Size-inclusive design with extended sizing options for better fit.",
            "Heritage-inspired workmanship using traditional techniques and patterns.",
            "Multifunctional design with hidden features and convertible elements.",
            "Zero-waste pattern cutting minimizes fabric waste during production.",
            "Gender-fluid design with versatile styling options for all identities.",
            "Regenerative materials sourced from environmentally positive practices.",
            "Adaptive clothing with accessible features for diverse needs and abilities.",
            "Biodegradable materials ensure environmentally friendly end-of-life cycle.",
            "Circular design principles for easy repair, recycling, or composting.",
            "Community-made with fair trade practices and artisan partnerships.",
            "Upcycled materials give new life to discarded fabrics and garments.",
            "Slow fashion approach with heirloom quality and timeless design.",
            "Local production supports regional economies and reduces transport impact.",
            "Digital printing technology creates vibrant, detailed patterns sustainably.",
            "Modular design allows components to be mixed, matched, or replaced.",
            "Smart textiles with integrated technology for enhanced functionality.",
            "Regenerative agriculture fibers grown with soil-health practices.",
            "Closed-loop system where garments can be returned for recycling.",
            "Plant-based dyes create beautiful colors without chemical pollutants."
        ]


        # Create 70 products with random data
        for i in range(70):


            # Random selection from available data
            title = random.choice(clothing_titles) + f" {random.choice(['Pro', 'Elite', 'Essential', 'Classic', 'Premium', 'Luxe'])}"
            price = round(random.uniform(29.99, 299.99), 2)
            size = random.choice(['0', '1', '2', '3'])  # M, L, XL, XXL
            
            # Decide on discount type
            has_discount = random.choice([True, False, False])  # 1/3 chance of having discount
            static_discount = None
            percent_discount = None
            
            if has_discount:
                discount_type = random.choice(['static', 'percent'])
                if discount_type == 'static':
                    static_discount = round(random.uniform(5.00, 50.00), 2)
                else:
                    percent_discount = random.randint(10, 50)
            
            description = random.choice(clothing_descriptions)
            
            # Create the product
            product = Product.objects.create(
                title = title,
                price = price,
                size = size,
                description = description,
                static_discount = static_discount,
                percent_dicount = percent_discount,
                # Note: image field will need to be handled separately
            )
            
            # Add random product features (assuming you already created ProductFeature objects)
            # Get random 3-7 features to add to each product
            all_features = ProductFeature.objects.all()
            num_features = random.randint(3, 7)
            random_features = random.sample(list(all_features), min(num_features, len(all_features)))
            product.product_features.set(random_features)
            
            print(f"Created product: {title}")
