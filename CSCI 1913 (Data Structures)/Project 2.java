// George Fisk Project 2

import java.util.Random;


     "club"     //  3
   };

  private int rank;  //  Card rank, between 0 and 12 inclusive.
  private int suit;  //  Card suit, between 0 and  3 inclusive.

//  CARD. Constructor. Make a new CARD with the given RANK and SUIT.

  public Card(int rank, int suit)
  {
    if (0 <= suit && suit <= 3 && 0 <= rank && rank <= 12)
    {
      this.rank = rank;
      this.suit = suit;
    }
    else
    {
      throw new IllegalArgumentException("No such card.");
    }
  }

//  GET RANK. Return the RANK of this card.

  public int getRank()
  {
    return rank;
  }

//  GET SUIT. Return the SUIT of this card.

  public int getSuit()
  {
    return suit;
  }

//  TO STRING. Return a string that describes this card, for printing only. For
//  example, we might return "the queen of diamonds" or "the ace of hearts".

  public String toString()
  {
    return "the " + rankName[rank] + " of " + suitName[suit] + "s";
  }
}

class Deck
{
	private Card[] cards;
	private int cardsDealt;
	
	public Deck()
	{
		cards = new Card[52];
		int i = 0;
		int j = 0;
		while (i < cards.length)
		{
			while (j < 4)
			{
				int r = i % cards.length;
				cards[i] = Card(r, j);
				i++;
				j++;
			}
			j = 0;
		}
	}
	
	public void shuffle()
	{
		if (cardsDealt > 0)
		{
			throw new IllegalStateExcpetion("Cards have already been dealt.");
		}
		Random r = new Random();
		int i = cards.length - 1;
		int j = Math.abs(r.nextInt())%i;
		while (i > 0)
		{
			Card temp = cards[i];
			cards[i] = cards[j];
			cards[j] = temp;
			i -= 1;
			j = Math.abs(r.nextInt())%i;
		}
		
	}
	
	public boolean canDeal()
	{
		return (cardsDealt <= 52);
	}
	
	public Card deal()
	{
		if !(canDeal())
		{
			throw new IllegalStateExcpetion("No cards remain.");
		}
		else
		{
			Card result = cards[cardsDealt]
			cardsDealt += 1;
			return result;
		}
	}
}

class Tableau
{
	private int size;
	private Pile first;
	
	private class Pile
	{
		private Card card;
		private Pile next;
		
		private Pile(Card card, Pile next)
		{
			this.card = card;
			this.next = next;
		}
		
	}
	
	public Tableau()
	{
		first = null;
		size = 0;
	}
	
	private void addPile(Card card)
	{
		Pile oldfirst = first;
		first = new Pile(card, oldfirst);
		size += 1;
		System.out.println("Added " + card.toString());
	}
	
	private boolean canMerge()
	{
		if (size < 2)
			return false;
		else
		{
			return canPutOn(first.card, first.next.card);
		}
	}
	
	private boolean canPutOn(Card left, Card right)
	{
		if (left.getSuit() == right.getSuit() || left.getRank() > right.getRank())
		{
			return true;
		}
		return false;
	}
	
	private boolean hasManyPiles()
	{
		return (size >= 2);
	}
	
	private void mergeTwoPiles()
	{
		first.next = first.next.next;
		size -= 1;
		System.out.println("Merged " + first.card.toString() + " and " + first.next.card.toString());
	}
	
	private void results()
	{
		if (hasManyPiles())
		{
			System.out.println("Lost the game.");
		}
		else
		{
			System.out.println("Won the game.");
		}
	}
	
	public void play()
	{
		Deck d = new Deck();
		addPile(d.deal());
		while (d.canDeal())
		{
			addPile(d.deal());
			while (canMerge())
			{
				mergeTwoPiles();
			}
		}
		results();
	}
}