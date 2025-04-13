import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Input } from '@/components/ui/input';
import { Button } from '@/components/ui/button';
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from '@/components/ui/card';

const Register = () => {
  const [handle, setHandle] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const response = await fetch('https://app-qfmuihch.fly.dev/users/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ handle }),
      });

      if (!response.ok) {
        throw new Error('Failed to create account');
      }

      const data = await response.json();
      
      localStorage.setItem('user', JSON.stringify(data));
      
      await fetch(`https://app-qfmuihch.fly.dev/itineraries/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_id: data.id }),
      });

      navigate('/public-itinerary');
    } catch (err) {
      setError('Failed to create account. Please try again.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gradient-to-b from-primary/20 to-accent/20">
      <div className="w-full max-w-md px-4">
        <Card className="w-full border-2 border-primary/30 shadow-lg">
          <CardHeader className="bg-primary/10 rounded-t-lg">
            <div className="flex flex-col items-center space-y-2">
              <h1 className="text-3xl font-bold text-center text-primary">Bali Trip</h1>
              <CardTitle className="text-center text-xl">April 16-24, 2025</CardTitle>
              <CardDescription className="text-center text-base">
                Create an account to view and select activities
              </CardDescription>
            </div>
          </CardHeader>
          <CardContent className="pt-6">
            <form onSubmit={handleSubmit}>
              <div className="space-y-4">
                <div className="space-y-2">
                  <label htmlFor="handle" className="text-sm font-medium">Username</label>
                  <Input
                    id="handle"
                    type="text"
                    placeholder="Enter your username"
                    value={handle}
                    onChange={(e) => setHandle(e.target.value)}
                    required
                    className="border-2 border-primary/30 focus:border-primary/50"
                  />
                </div>
                {error && <p className="text-sm text-destructive">{error}</p>}
                <Button type="submit" className="w-full" disabled={loading}>
                  {loading ? 'Creating Account...' : 'Create Account'}
                </Button>
              </div>
            </form>
          </CardContent>
          <CardFooter className="flex justify-center bg-accent/10 rounded-b-lg">
            <p className="text-sm text-muted-foreground">
              No password required. Just enter a username to get started.
            </p>
          </CardFooter>
        </Card>
      </div>
    </div>
  );
};

export default Register;
