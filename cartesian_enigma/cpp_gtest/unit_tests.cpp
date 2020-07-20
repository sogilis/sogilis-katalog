#include <gtest/gtest.h>
#include "decoder.hpp"

TEST(DecoderSuite, sample_case)
{
	ASSERT_EQ("42", decode("Anything goes.."));
}
