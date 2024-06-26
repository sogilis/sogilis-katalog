defmodule ElixirAnagrams do
  @moduledoc """
  Elixir implementation of http://codekata.com/kata/kata06-anagrams/
  """

  @wordlist "../../wordlist.txt"

  def load_word_list() do
    @wordlist
    |> Path.expand(__DIR__)
    |> File.stream!
    |> Stream.map(&(String.replace(&1, "\n", "")))
  end

  defp hash(word) do
    String.to_charlist(word) |> Enum.sort
    rescue
      _ -> :not_utf8
  end

  defp insert_word_by_size(word, map) do
    hash = hash(word)
    case Map.fetch(map, hash) do
      :error -> Map.put(map, hash, [word])
      {:ok, list} -> Map.put(map, hash, Enum.concat(list, [word]))
    end
  end

  @doc """
  ## Examples
      iex> ElixirAnagrams.run
      ["acoustoelectrically", "electroacoustically"]

  """
  def run() do
    load_word_list()
    |> Enum.reduce(%{}, &insert_word_by_size/2) #let operate by word size
    |> Map.values
    |> Enum.reject(fn l -> Enum.count(l) < 2 end)
    |> Enum.max_by(fn l -> String.length(Enum.at(l, 0)) end)
  end
end
