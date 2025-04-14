export interface User {
  email: string;
  id: string;
}

export interface Activity {
  id: string;
  title: string;
  description: string;
  date: string; // Format: YYYY-MM-DD
  time: string; // Format: HH:MM
  location: string;
  category: string;
}

export interface Itinerary {
  userId: string;
  activities: string[]; // Array of activity IDs
}
