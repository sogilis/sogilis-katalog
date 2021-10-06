
#include "gtest/gtest.h"

#include "decoder.h"

namespace cartesian_enigma_test {

	class TestFixtureDecoder : public ::testing::Test {
	protected:
		// You can do set-up work for each test here.
		TestFixtureDecoder();

		// You can do clean-up work that doesn't throw exceptions here.
		virtual ~TestFixtureDecoder();

		// If the constructor and destructor are not enough for setting up
		// and cleaning up each test, you can define the following methods:

		// Code here will be called immediately after the constructor (right
		// before each test).
		virtual void SetUp();

		// Code here will be called immediately after each test (right
		// before the destructor).
		virtual void TearDown();

		cartesian_enigma::Decoder cartesianEnigma;
	};
}

using namespace cartesian_enigma_test;

TestFixtureDecoder::TestFixtureDecoder(): cartesianEnigma(){}

TestFixtureDecoder::~TestFixtureDecoder() {};

void TestFixtureDecoder::SetUp() {};

void TestFixtureDecoder::TearDown() {};

TEST_F(TestFixtureDecoder, TestHello) {
    EXPECT_EQ(cartesianEnigma.hello(), 0);
}


