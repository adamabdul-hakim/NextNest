import {createClient} from "@supabase/supabase-js"

const URL = "https://gljqgghjwuyzspjjgchp.supabase.co"
const API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdsanFnZ2hqd3V5enNwampnY2hwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMzNzc5ODgsImV4cCI6MjA2ODk1Mzk4OH0.WOvcLQUb1Niv_Sa1OvKvT7DhtOWwZkqMEkrIVHl9N9M"

export const supabase = createClient(URL, API_KEY)