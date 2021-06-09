#[cfg(test)]
mod cartesian_test {
    use super::super::cartesian_decoder;

    #[test]
    fn decode_single_letter() {
        assert_eq!(cartesian_decoder(&String::from("AB")), "AB");
    }

    #[test]
    fn decode_two_letters() {
        assert_eq!(cartesian_decoder(&String::from("ABCD")), "ABCD");
    }
}
