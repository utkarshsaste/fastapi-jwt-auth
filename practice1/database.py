from supabase import create_client

SUPABASE_URL = "https://pyvfduogxwrcjchaupwt.supabase.co"
SUPABASE_KEY = "sb_publishable_LRDga9yp_cBwwxQaKzaJFA_w0Dj9KL-"

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)